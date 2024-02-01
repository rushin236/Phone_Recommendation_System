import re

import numpy as np
import pandas as pd

from phone_recommender.components.data_extraction import DataExtraction
from phone_recommender.config.configuration import ConfigurationManager


class DataExtractionPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_extraction_config = config.get_data_extraction_config()
        data_extraction = DataExtraction(data_extraction_config)
        df = data_extraction.get_local_data()
        df["text"] = df["text"].str.lower()
        df["network"] = df["text"].apply(lambda x: get_network(x))
        drop_idx = df[df["network"] == "0"].index
        df = df.drop(index=drop_idx)
        df["4g_bands"] = df["text"].apply(lambda x: get_4g_bands(x))
        df["4g_band_count"] = df["4g_bands"].apply(lambda x: get_bands_count(x))
        df["5g_bands"] = df["text"].apply(lambda x: get_5g_bands(x))
        df["5g_band_count"] = df["5g_bands"].apply(lambda x: get_bands_count(x))
        df["released_year"] = df["text"].apply(lambda x: get_released_year(x))
        df["height_width_depth"] = df["text"].apply(lambda x: get_full_dimension(x))
        df[["height", "width", "depth"]] = df["height_width_depth"].apply(
            lambda x: get_hwd(x)
        )
        df["weight"] = df["text"].apply(lambda x: get_weight(x))
        df[["resolution", "ppi"]] = df["text"].apply(lambda x: get_resolution(x))
        df[["display_width", "display_height"]] = df["resolution"].apply(
            lambda x: get_resolution_wh(x)
        )
        df["display_ppi"] = df["ppi"].apply(lambda x: get_ppi(x))
        df["display_size_str"] = df["text"].apply(lambda x: display_size_str(x))
        df["display_size"] = df["text"].apply(lambda x: display_size(x))
        df["display_type"] = df["text"].apply(lambda x: display_type(x))
        df["os"] = df["text"].apply(lambda x: get_os(x))
        df["chipset"] = df["text"].apply(lambda x: get_chipset(x))
        df[["ram", "storage", "type"]] = df["text"].apply(lambda x: get_memory(x))
        df["main_camera"] = df["text"].apply(lambda x: get_main_camera(x))
        df["selfie_camera"] = df["text"].apply(lambda x: get_selfie_camera(x))
        df["bluetooth"] = df["text"].apply(lambda x: get_comms(x))
        df["battery"] = df["text"].apply(lambda x: get_battery(x))
        df["price"] = df["text"].apply(lambda x: get_price(x))
        df["price"] = df["price"].apply(lambda x: get_price_int(x))
        data_extraction.save_extracted_data(df=df)


def get_network(string):
    res = re.search(r"network.*2g bands", string)
    if res is not None:
        network = re.sub(r"network technology|2g bands|\/|gsm", "", res.group()).strip()
        if ("lte" in network) or "5g" in network or "4g" in network:
            network = re.sub(
                r"cdma|hspa|cdma|cdma2000|evdo|2000|umts", "", network
            ).strip()
            # print(network)
            return network
        else:
            # print("0")
            return "0"
    else:
        # print("0")
        return "0"


def get_4g_bands(text):
    pattern = re.compile(r"4g bands.*speed|4g bands.*5g")
    bands_4g = re.search(pattern, text)
    if bands_4g is not None:
        bands = re.sub(r"4g bands|speed|5g bands.*|", "", bands_4g.group()).strip()
        if "lte" not in bands:
            bands = re.findall(r"\d,|\d\d,", bands)
            if len(bands) not in [0, 1]:
                bands = " ".join(bands)
                bands = re.sub(",", "", bands)
                bands = " ".join(
                    [str(x) for x in sorted(([int(x) for x in set(bands.split())]))]
                )
                # print(bands)
                return bands
            else:
                # print("1")
                return "1"
        else:
            # print("1")
            return "1"


def get_bands_count(text):
    if text not in ["1", "0"]:
        band_count = len(text.split())
        # print(band_count)
        return band_count
    elif text == "1":
        # print(1)
        return 1
    else:
        return 0


def get_5g_bands(text):
    res = re.search(r"5g bands.*speed|5g bands.*announced", text)
    if res is not None:
        bands = re.sub("5g bands|speed", "", res.group()).strip()
        bands = re.sub(r"sa/nsa|sa/nsa/sub6", "1,", bands).strip()
        bands = re.findall(r"\d,|\d\d,|\d\d\d,", bands)
        if len(bands) not in [0, 1]:
            bands = " ".join(bands)
            bands = re.sub(",", "", bands)
            bands = " ".join(
                [str(x) for x in sorted(([int(x) for x in set(bands.split())]))]
            )
            # print(bands)
            return bands
        else:
            # print("1")
            return "1"
    else:
        # print("0")
        return "0"


def get_released_year(text):
    pattern = re.compile(r"status.*dimensions")
    res = re.search(pattern=pattern, string=text)
    if res is not None:
        res = re.sub(
            r",|status|dimensions|available. released|body", "", res.group()
        ).strip()
        if res not in ["discontinued", "cancelled"]:
            # print(res.split()[0])
            return res.split()[0]
        else:
            # print(res)
            return res
    else:
        # print('0')
        return "no info"


def get_full_dimension(string):
    pattern = re.compile(r"dimensions.*weight")
    res = re.search(pattern=pattern, string=string).group()
    if res is not None:
        res = re.sub(
            r"dimensions|weight|mm.*|unfolded|or.*|cc|\(.*|-.*|:|x", "", res
        ).strip()
        if len(res.split()) == 3:
            # print(res)
            return " ".join(res.split())
        else:
            # print("0 x 0 x 0")
            return "0 0 0"
    else:
        # print("0 x 0 x 0")
        return "0 0 0"


def get_hwd(text):
    res = (
        [0.0, 0.0, 0.0]
        if text == "0 0 0"
        else [round(float(x), 1) for x in text.split()]
    )
    return pd.Series(res, index=["height", "width", "depth"])


def get_weight(string):
    res = re.search(r"weight.*sim|weight.*build", string)
    if res is not None:
        weight = re.search(r"\d\d\d g|\d\d g", res.group())
        if weight is not None:
            weight = re.sub(r"g", "", weight.group()).strip()
            return weight
        else:
            # print("0")
            return "0"
    else:
        # print("0")
        return "0"


def get_resolution(string):
    res = re.search(r"resolution.*protection|resolution.*os", string)
    if res is not None:
        resolution = re.search(r"resolution.*pixels", res.group())
        ppi = re.search(r"\(~.* ppi", res.group())
        if resolution and ppi is not None:
            resolution = " ".join(
                re.sub(r",.*|\(.*|pixels.*|resolution|:|x", "", resolution.group())
                .strip()
                .split()
            )
            ppi = re.sub(r"\(~|ppi", "", ppi.group()).strip()
            # print([resolution, ppi])
            return pd.Series([resolution, ppi], index=["resolution", "ppi"])
        else:
            # print(["0 0", "0 ppi"])
            return pd.Series(["0 0", "0"], index=["resolution", "ppi"])
    else:
        # print(["0 0", "0 ppi"])
        return pd.Series(["0 0", "0"], index=["resolution", "ppi"])


def get_resolution_wh(resolution):
    res = resolution.split()
    return pd.Series(
        [float(res[0]), float(res[1])], index=["display_width", "display_height"]
    )


def get_ppi(ppi):
    res = ppi
    return float(res)


def display_size_str(string):
    res = re.search(r"size.*inches,", string)
    if res is not None:
        res = re.sub(r"size|inches,.*", "", res.group()).strip()
        res = str(round(float(res), 1))
        # print(res)
        return res
    else:
        # print("0")
        return "0"


def display_size(string):
    res = re.search(r"size.*inches,", string)
    if res is not None:
        res = re.sub(r"size|inches,.*", "", res.group()).strip()
        res = round(float(res), 1)
        # print(res)
        return res
    else:
        # print("0")
        return 0


def display_type(text):
    res = re.search(r"display type.*size", text)
    if res is not None:
        display_type = re.sub(
            r"display type|size|,|\(|\)|2x|international.*|hdr10|\+|ical|plus|hdr|[0-9bk]{2,4} colors|flexible|dynamic|foldable|[0-9]{3,4} nits|dolby vision|typ|hbm|peak",
            "",
            res.group(),
        ).strip()
        display_type = re.sub(r"amoled", "oled", display_type).strip()
        display_type = " ".join(display_type.split())
        # print(display_type)
        return display_type
    else:
        # print("no info")
        return "no info"


def get_os(text):
    res = re.search(r"os.*chipset", text)
    if res is not None:
        platform = re.sub(
            r"os|chipset|oreo|pie|or.*|,.*|\(.*|\/.*", "", res.group()
        ).strip()
        if platform.split()[0] in ["5433)hspa", "t"]:
            platform = re.sub(r"5433\)hspa 42\.2\/5\.76 mbps|t.*", "0", platform)
        # platform = re.sub(r"5433)hspa 42.2/5.76 mbps", "0", platform).strip()
        # print(platform)
        return "".join(platform.split())
    else:
        # print("0")
        return "0"


def get_chipset(text):
    res = re.search(r"chipset.*", text)
    if res is not None:
        chipset = re.search(
            r"kirin [0-9a-z]{2,5}|snapdragon [0-9+gens ]{2,8}|dimensity [0-9]{2,5}|exynos [0-9]{2,4}|helio [0-9pgax]{1,4}",
            res.group(),
        )
        if chipset is not None:
            chipset = re.sub(r" 5g| 4g", "", chipset.group())
            # print(chipset)
            return "".join(chipset.split())
        else:
            # print("0")
            return "0"
    else:
        # print("0")
        return "0"


def get_memory(text):
    res = re.search(r"memory.*main camera", text)
    if res is not None:
        res = re.sub(r".*internal|main.*|\(.*\)|- india|\.x|\d+mb", "", res.group())
        ram = " ".join(np.unique(re.findall(r"\dgb ram|\d\dgb ram", res)))
        stg = re.sub(r"\dgb ram|\d\dgb ram|,|1\.|sfs|umcp|emcp|", "", res).strip()
        ram = re.sub(r"ram", "", ram)
        type = re.search(r"ufs.*|emmc.*", stg)
        if type is not None:
            stg = re.sub(r"ufs.*|emmc.*|sfs|umcp", "", stg)
            stg = " ".join(np.unique(stg.split()))
            type = re.sub(r"or.*", "", "".join(type.group().strip().split()))
            # print(ram, stg, type)
            return pd.Series([ram, stg, type], index=["ram", "storage", "type"])
        elif (ram == "") and (stg != ""):
            # print(f"0 {stg} 0")
            return pd.Series(["0", stg, "0"], index=["ram", "storage", "type"])
        else:
            stg = " ".join(np.unique(stg.split()))
            # print(ram, stg)
            return pd.Series([ram, stg, "0"], index=["ram", "storage", "type"])
    else:
        # print("0 0 0")
        return pd.Series(["0", "0", "0"], index=["ram", "storage", "type"])


def get_main_camera(text):
    res = re.search(r"main camera.*", text)
    if res is not None:
        main_camera = re.sub(
            r"main camera|selfie.*|,|\/|\(|\)|\"|triple|dual|single|feature|video|quad",
            "",
            res.group(),
        ).strip()
        main_camera = re.search(r"\d mp|\d\d mp|\d\d\d mp", main_camera)
        if main_camera is not None:
            # print(main_camera.group())
            return "".join(main_camera.group().strip().split())
        else:
            # print("0")
            return "0"
    else:
        # print('0')
        return "0"


def get_selfie_camera(text):
    res = re.search(r"selfie camera.*", text)
    if res is not None:
        selfie_camera = " ".join(
            re.sub(
                r"sound.*|selfie camera|single|dual|\/|\(|\)|\"|,|-|video",
                "",
                res.group(),
            )
            .strip()
            .split()
        )
        selfie_camera = re.search(r"\d mp|\d\d mp|\d\d\d mp", selfie_camera)
        if selfie_camera is not None:
            # print(selfie_camera.group())
            return "".join(selfie_camera.group().strip().split())
        else:
            # print("0")
            return "0"
    else:
        # print("0")
        return "0"


def get_comms(text):
    res = re.search(r"comms.*", text)
    if res is not None:
        comms = re.sub(
            r"positioning.*|,|dual-band|comms|wlan|wi-fi|wi-fi direct|a2dp|le",
            "",
            res.group(),
        ).strip()
        bluetooth = re.search(r"bluetooth [0-9.yesno]{1,4}", comms)
        if bluetooth is not None:
            # print(bluetooth.group())
            return "".join(bluetooth.group().strip().split())
        else:
            # print("0")
            return "0"
    else:
        # print('0')
        return "0"


def get_battery(text):
    battery_mah = re.search(r"\d\d\d\d mah", text)
    if battery_mah is not None:
        # print(battery_mah.group())
        return "".join(battery_mah.group().strip().split())
    else:
        # print("0")
        return "0"


def get_price(text):
    price = re.search(r"price.*", text)
    if price is not None:
        price = re.search(
            r"\d\d\d eur|\d\d eur|€ [0-9.,]{2,10}|₹ [0-9,]{2,10}", price.group()
        )
        if price is not None:
            return price.group().strip()
        else:
            return "0"
    else:
        return "0"


def get_price_int(price):
    if "₹" in price:
        price = re.sub(r"₹|,", "", price)
        # print(round(float(price), 0))
        return round(float(price), 0)
    elif "€" in price:
        price = re.sub(r"€|,", "", price)
        # print(round(float(price), 0) * 89)
        return round(float(price), 0) * 89
    elif "eur" in price:
        price = re.sub(r"eur|,", "", price)
        # print(round(float(price), 0) * 89)
        return round(float(price), 0) * 89
    else:
        # print(0)
        return 0
