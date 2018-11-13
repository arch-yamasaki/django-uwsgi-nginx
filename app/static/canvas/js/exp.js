
// var limePlot1 = [
//     { indexLabel: "2000 < PCR",   y: 0.20 , x:2 },
//     { indexLabel: "ALB < 3.3", y: 0.10 , x:3},
//     { indexLabel: "ALB < 3.4", y: 0.07 , x:4},
//     { indexLabel: "1500 < PCR < 2200", y: 0.04, x:5 },
//     { indexLabel: "K > 20",   y: 0.02 , x:6},
//     //  { indexLabel: "TP > 6.3", y: -0.05 },
//     //  { indexLabel: "PCR < 1200 " , y: -0.02 },
//   ];
  
  var limePlot2 = [
    { indexLabel: "TP > 6.3", y: -0.05 , x: 1},
    { indexLabel: "PCR < 1200 " , y: -0.02 , x: 0}
  ];
  
  var chart = new CanvasJS.Chart("chartContainer", {
    
    title:{
      text: "LIME Result"
    },
    // hide axisX label
    axisX:{
      valueFormatString: " ",
      tickLength: 0
    },
    
    axisY:{
      minimum: - 0.3,
      maximum: 0.3,
    },
    
    // ここにグラフ作成処理を書く
    data: [
      {
      // グラフの種類. barなら横棒グラフ
      type:"bar",
      
      // 色の説明をしてくれる。Datasereis2  なので non-nephrosisに変更したい。
      showInLegend: true,
      //ここにデータを渡す
      dataPoints: limePlot1,
      
      },
      {
      type:"bar",
      showInLegend: true,
      dataPoints: limePlot2
      }
    ]
  
  });
  
  chart.render();
  
  //if(chart.options.data.length === 1) {
  //  chart.data[0].set("color", "#369EAD"); // custom color to be set
  //} 