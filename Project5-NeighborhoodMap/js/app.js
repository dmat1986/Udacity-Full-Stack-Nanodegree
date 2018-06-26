var map;

var clientID = '5XTXNNQYL011RTYIAMMM4R2KFGBQE2M4X5ZH23CHS0LFAG02';
var clientSecret = 'RNOJHEQBHH1GPR0RRN5SJHTM1HEPNUQ0JLSJQOCDOAI55KBG';

var locations = [
      {title: 'CN Tower', lat: 43.6426, lng: -79.3871},
      {title: 'Rogers Center', lat: 43.6414, lng: -79.3894},
      {title: 'CNE',lat: 43.6331, lng: -79.4226},
      {title: 'Billy Bishop Toronto City Airport', lat: 43.6285, lng: -79.3960},
      {title: 'University of Toronto', lat: 43.6629, lng: -79.3957},
      {title: 'Yonge & Dundas Square', lat: 43.6562, lng: -79.3806}
];

function errorHandler() {
    $('#map').html('Google Maps could not load. Please try again.');
}

//Foursquare setup
var Place = function(info) {
    var self = this;
    this.URL = '';
    this.title = info.title;
    this.lat = info.lat;
    this.lng = info.lng;
    this.street = '';
    this.city = '';

    // Make markers visible
    this.visible = ko.observable(true);

    var fsURL = 'https://api.foursquare.com/v2/venues/search?ll=' + this.lat + ',' + this.lng + '&client_id=' + clientID + '&client_secret=' + clientSecret + '&v=20180620' + '&query=' + this.title;

    // Get Foursquare info
    $.getJSON(fsURL).done(function (info) {
        var results = info.response.venues[0];
        self.URL = results.url;
        if (typeof self.URL === 'undefined') {
            self.URL = "";
        }
        self.street = results.location.formattedAddress[0] || 'No Address Provided';
        self.city = results.location.formattedAddress[1] || 'No Address Provided';
    }).fail(function () {
        $('.list').html('The Foursquare API could not load. Please try again.');
    });

    // largeInfoWindow info on click.
    this.contentString = '<div class="info-window-content"><div class="title"><b>' + info.title + "</b></div>" +
        '<div class="content"><a href="' + self.URL + '">' + self.URL + "</a></div>" +
        '<div class="content">' + self.street + "</div>" +
        '<div class="content">' + self.city + "</div>";

    // Puts the content string inside largeInfoWindow.
    this.largeInfoWindow = new google.maps.InfoWindow({
        content: self.contentString
    });

    // Places the marker to it's appropriate location
    this.marker = new google.maps.Marker({
        position: new google.maps.LatLng(info.lat, info.lng),
        map: map,
        title: info.title
    });

    this.showMarker = ko.computed(function() {
        if(this.visible() === true) {
            this.marker.setMap(map);
        } else {
            this.marker.setMap(null);
        }
        return true;
    }, this);

    // Add largeInfoWindow to marker when clicked
    this.marker.addListener('click', function(){
        self.contentString = '<div class="info-window-content"><div class="title"><b>' + info.title + "</b></div>" +
            '<div class="content"><a href="' + self.URL +'">' + self.URL + "</a></div>" +
            '<div class="content">' + self.street + "</div>" +
            '<div class="content">' + self.city + "</div>";

        self.largeInfoWindow.setContent(self.contentString);

        self.largeInfoWindow.open(map, this);

        self.marker.setAnimation(google.maps.Animation.BOUNCE);
        setTimeout(function() {
            self.marker.setAnimation(null);
        }, 1000);
    });

    // Adds animation to marker when clicked
    this.bounce = function(place) {
        google.maps.event.trigger(self.marker, 'click');
    };
};

var ViewModel = function () {
    var self = this;

    this.search_filter = ko.observable('');

    this.list = ko.observableArray([]);

    // Create a styles array to use with the map.
    var styles = [
     {
        featureType: 'water',
        stylers: [
          { color: '#19a0d8' }
        ]
      },{
        featureType: 'administrative',
        elementType: 'labels.text.stroke',
        stylers: [
          { color: '#ffffff' },
          { weight: 6 }
        ]
      },{
        featureType: 'administrative',
        elementType: 'labels.text.fill',
        stylers: [
          { color: '#e85113' }
        ]
      },{
        featureType: 'road.highway',
        elementType: 'geometry.stroke',
        stylers: [
          { color: '#efe9e4' },
          { lightness: -40 }
        ]
      },{
        featureType: 'transit.station',
        stylers: [
          { weight: 9 },
          { hue: '#e85113' }
        ]
      },{
        featureType: 'road.highway',
        elementType: 'labels.icon',
        stylers: [
          { visibility: 'off' }
        ]
      },{
        featureType: 'water',
        elementType: 'labels.text.stroke',
        stylers: [
          { lightness: 100 }
        ]
      },{
        featureType: 'water',
        elementType: 'labels.text.fill',
        stylers: [
          { lightness: -100 }
        ]
      },{
        featureType: 'poi',
        elementType: 'geometry',
        stylers: [
          { visibility: 'on' },
          { color: '#f0e4d3' }
        ]
      },{
        featureType: 'road.highway',
        elementType: 'geometry.fill',
        stylers: [
          { color: '#efe9e4' },
          { lightness: -25 }
        ]
      }
    ];

    // Constructor creates a new map - only center and zoom are required.
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 43.6532, lng: -79.3832},
        zoom: 13,
        styles: styles,
        mapTypeControl: false
    });

    locations.forEach(function(item){
        self.list.push( new Place(item));
    });

    // filers the default locations based on user search
    this.filter_array = ko.computed( function() {
        var filter = self.search_filter().toLowerCase();
        if (!filter) {
            self.list().forEach(function(item){
                item.visible(true);
            });
            return self.list();
        } else {
            return ko.utils.arrayFilter(self.list(), function(item) {
                var string = item.title.toLowerCase();
                var result = (string.search(filter) >= 0);
                item.visible(result);
                return result;
            });
        }
    }, self);
};

function initMap() {
    ko.applyBindings(new ViewModel());
}