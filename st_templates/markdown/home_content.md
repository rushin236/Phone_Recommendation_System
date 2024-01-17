<style>
    #home-content {
        width: 70%;
        display: flex;
        flex-direction: column;
        gap: 1.5rem;
        margin: auto;
    }

    h1,
    h2,
    h3,
    h4 {
        text-align: center;
    }

    p {
        font-size: 1.2rem;
        text-align: center;
    }

    #processor-content,
    #ram-content,
    #storage-content,
    #software-content {
        display: flex;
        flex-direction: row;
        gap: 10%;
    }

    .p-content li,
    .r-content li,
    .s-content li,
    .so-content li {
        font-size: 1.1rem;
    }

    .p-img-content,
    .r-img-content,
    .s-img-content,
    .so-img-content,
    .p-content,
    .r-content,
    .s-content,
    .so-content {
        margin: auto;
    }

    .p-img-content img,
    .r-img-content img,
    .s-img-content img,
    .so-img-content img {
        padding: 0.5rem;
        border-radius: 20px;
        height: 400px;
        width: 400px;
    }
</style>

<div id="home-content">
<h1> Phone Recommendation </h1>

<h2> Introduction </h2>
    
<ul>
    <p>
        In today's fast-paced world, having the right smartphone can significantly enhance your home experience. Whether you're a tech enthusiast or just looking for a reliable device, we've got you covered. This recommendation system is designed to suggest phones that are best suited for your requirements and need's.
    </p>
    <p>
        A lot of people don't have the technical knowledge of phone specification, so many of them end up buying the wrong device which is not up to their expectations, so as a tech and data science enthusiast I have build a recommendation system that will help up guide and buy the right phone you desire.
    </p>
</ul>

<h2> What to look for while buying phone? </h2>

<h3> Processor (CPU) </h3>
<div id="processor-content">
<div class="p-content">
    <ul>
        <p>
            It is the heart and core of your device.
        </p>
        <p>
            The processor handles all the task that you perform on your device whether it gaming, watching content scrolling through social media etc...
        </p>
        <p>
            A processor consists of many things, I will be explaining you the most important and that's all you will ever need.
        </p>
    </ul>
    <h4> Clock Speed </h4>
    <ul>
        <li> 
            It is the usually denoted by Ghz in the phone specification.
        </li>
        <li> 
            It means how fast your phone can perform a given task. 
        </li>
        <li> 
            Higher the clock speed of processor the better it is, it is applicable for all the processor with respect to their <strong>cpu architecture.</strong> 
        </li>
        <li> 
            To know more about arm64 which is used in mobile devices like smartphones click <a href="https://en.wikipedia.org/wiki/ARM_architecture_family#64/32-bit_architecture">here</a>
        </li>
    </ul>
    <h4> Process node (Semiconductor device fabrication) </h4>
    <ul>
        <li> 
            It is usually denoted by (nm) meaning nano meter.
        </li>
        <li> 
            The smaller the process node the better is the performance and efficiency of a processor. 
        </li>
        <li> 
            Currently the no going process node on which processors are made is 4nm. 
        </li>
        <li> 
            You will always find it near the CPU specification.
        </li>
    </ul>    
</div>
<div class="p-img-content">
    <img src="https://github.com/rushin236/Phone_recommendation_system/blob/main/st_static/images/processor-image.png?raw=true" alt="Processor Image">
</div>
</div>

<h3> Random Access Memory (RAM) </h3>
<div id="ram-content">
<div class="r-img-content">
    <img src="https://github.com/rushin236/Phone_recommendation_system/blob/main/st_static/images/ram-image.png?raw=true" alt="Ram Image">
</div>
<div class="r-content">
    <ul>
        <p> 
            It is basically a component that denotes how many application your device can run in background. 
        </p>
        <p> 
            The more ram a device has the more applications it can run in background with out closing them. 
        </p>
    </ul>
    <h4> How to get the right one? </h4>
    <ul>
        <li> 
            In todays world with applications using AI and so many other technologies, my recommendation is to go with at least 8GB RAM.
        </li>
        <li> 
            RAM also has speed to as a processor has clock speed.. 
        </li>
        <li> 
            Speed of RAM is usually denoted by LPDDR followed by a number. 
        </li>
        <li> 
            Higher the number after LPDDR better will be the performance and efficiency of the RAM.
        </li>
    </ul>  
</div>
</div>

<h3> Read Only Memory (ROM) </h3>
<div id="storage-content">
<div class="s-content">
    <ul>
        <p> 
            The storage size totally depends on user's need, but my recommendation is to go with at least 128GB storage in todays world as the size of applications and files is growing with every update. 
        </p>
        <p> 
            It is like the storage room in our home. 
        </p>
        <p> 
            It keeps all the application, file and media files.
        </p>
    </ul>
    <h4> Type of storage </h4>
    <ul>
        <h4> EMMC </h4>
        <ul>
            <li> 
                This is a type of storage which is good but not as fast as ufs.
            </li>
            <li> 
                Most of the brands, e-commerce sites or the retail shops won't tell customers about the type of storage, so you your self have to find the type visiting sites like <a href="https://www.gsmarena.com/">gsmarena</a> or <a href="https://www.91mobiles.com/">91mobiles</a> these sites have all the info, and even if these sites don't have the info then most probably the brand has not mentioned it. 
            </li>
            <li> 
                For EMMC type storage it is most probably mentioned as EMMC followed by a number (example EMMC 5.1) the greater the number, better the storage in terms of performance and efficiency. 
            </li>
        </ul>
        <h4> UFS </h4>
        <ul>
            <li> 
                It is the fasted storage available on the market in terms of speed, efficiency and reliability.
            </li>
            <li> 
                UFS storage is also denoted as UFS followed by a number (example UFS 3.1), and greater the number better the performance and efficiency. 
            </li>
        </ul>
    </ul>
</div>
<div class="s-img-content">
    <img src="https://github.com/rushin236/Phone_recommendation_system/blob/main/st_static/images/storage-image.png?raw=true" alt="Storage Image">
</div>
</div>

<h3> Software </h3>
<div id="software-content">
<div class="so-img-content">
    <img src="https://github.com/rushin236/Phone_recommendation_system/blob/main/st_static/images/software-image.png?raw=true" alt="Storage Image">
</div>
<div class="so-content">
    <ul>
        <p> 
            It is the component that help you to perform task and interact with your devices hardware.
        </p>
    </ul>
    <h4> Which is the right one? </h4>
    <ul>
        <li> 
            It is basically a personal preference and does not matter, which one you choose.
        </li>
        <li> 
            The only difference is the skin above android which has a different look and feel to it for every brand.
        </li>
        <li> 
            Also the brands like mi and realme are able to sell there phones at cheaper price then others because they include bloatware and other brands don't.
        </li>
        <li> 
            It also plays an import roll in terms of software experience, as the bloatware tends to track your activities and based on these show you ab's.
        </li>
        <li> 
            So the to get a clean software experience I recommend to buy a phone with stock android.
        </li>
        <li> 
            Also look for the support of camera to API for installing gcam mods which will help you click so better photos with different XML files.
        </li>
    </ul>
</div>
</div>

<h3> Conclusion </h3>
<ul>
    <p>
        This is all you need to check for getting a better phone that last's you long, is good in terms for performance and efficiency, and is reliable.
    </p>
</ul>

</div>
