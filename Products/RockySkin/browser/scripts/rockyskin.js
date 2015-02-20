var rvs_collection_loader;

rvsCollectionResizer = function () {
  'use strict';
  var column, ctop, cheight, collection, newheight, listing, lheight,
      actions, aheight;
  lheight = aheight = 0;
  if ($('body.portaltype-topic').length > 0) {
      // calculate the distance from the top of the page to the bottom of the
      // left portlet column
      column = $('td#portal-column-one div.visualPadding');
      if (column.length > 0) {
          ctop = column.offset().top;
          cheight = column.height();
          // grab the collection dl and, if present, the height of the elements
          // below it
          collection = $('div#content-core dl');
          if (collection.length > 0) {
              listing = $('div#content-core div.listingBar');
              actions = $('div.documentActions');
              if (listing.length > 0) {
                  lheight = listing.height();
              }
              if (actions.length > 0) {
                  aheight = actions.height();
              }
              // new height = total column height - top of collection - height of elements below collection
              newheight = ((ctop + cheight) - collection.offset().top - (lheight + aheight));
              // on the off chance that the difference ends up being too small, 
              // default to the former height.  This is better that ending up with 
              // a negatively-sized element, or one too small to see anything.
              if (newheight < 200) {
                  newheight = 200;
              }
              collection.height(newheight);
          }
      }
  }
};

$(window).load(function () {
    // 'use strict';
    var interval_timeline = false;
    if ($('.twitter-timeline').length) {
        interval_timeline = setInterval(function(){
            console.log($('.twitter-timeline').width());
            if ($('.twitter-timeline').hasClass('twitter-timeline-rendered')) {
                if ($('.twitter-timeline').width() > 10) {
                    //Callback
                    clearInterval(interval_timeline);
                    window.rvsCollectionResizer();
                }
            }
        }, 200)
    } else {
        window.rvsCollectionResizer();
    }
});
