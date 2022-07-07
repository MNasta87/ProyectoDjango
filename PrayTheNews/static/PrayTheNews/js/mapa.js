
    
    function initMap() {
        
        const uluru = { lat: -33.3666818, lng: -70.6745619 };
       
        const map = new google.maps.Map(document.getElementById("map"), {
            zoom: 16,
            center: uluru,
        });
        
        const marker = new google.maps.Marker({
            position: uluru,
            map: map,
        });
    }

    window.initMap = initMap;


