function drawViz(vizData){
    var height = dscc.getHeight();
    var width = dscc.getWidth();
    console.log(vizData);
    // this is where you write your viz code
  }
  
  dscc.subscribeToData(drawViz, {transform: dscc.objectTransform})
  