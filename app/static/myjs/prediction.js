var chart = new CanvasJS.Chart("predictionContainer", {
    
    title:{
      text: "prediction proba"
    },
    // hide axisX label
    axisX:{
      valueFormatString: " ",
      tickLength: 0
    },
    
    axisY:{
      minimum: 0,
      maximum: 1.0,
    },
    
    // ここにグラフ作成処理を書く
    data: [
      {
      // グラフの種類. barなら横棒グラフ
      type:"bar",
      
      // 色の説明をしてくれる。Datasereis2  なので non-nephrosisに変更したい。
      showInLegend: true,
      //ここにデータを渡す
      dataPoints: predictionPlot,
      
      },
    ]
  
  });
  
  chart.render();
  