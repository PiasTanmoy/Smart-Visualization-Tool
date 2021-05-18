


  window.addEventListener('load', setup);

  async function setup() {

    const ctx = document.getElementById('myChart').getContext('2d');
    const ctx2 = document.getElementById('myChart2').getContext('2d');
    const ctx3 = document.getElementById('myChart3').getContext('2d');
    const ctx4 = document.getElementById('myChart4').getContext('2d');
    const ctx5 = document.getElementById('myChart5').getContext('2d');
    const ctx6 = document.getElementById('myChart6').getContext('2d');

    const dataTemps = await getData();

    const myChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: dataTemps.dates,
        datasets: dataTemps.all_data
      },
      options: {
          onClick: (e) => {
            const canvasPosition = Chart.helpers.getRelativePosition(e, chart);

            // Substitute the appropriate scale IDs
            const dataX = myChart.scales.xAxes.getValueForPixel(canvasPosition.x);
            const dataY = myChart.scales.yAxes.getValueForPixel(canvasPosition.y);
        },
          events: ['mousemove', 'mouseout', 'click', 'touchstart', 'touchmove'],
          animations: {
              tension: {
                  duration: 1000,
                  easing: 'linear',
                  from: 0.3,
                  to: 0,
                  loop: false
              },
              events: ['click']
          },
          scales: {
            yAxes: [{
                ticks: {
                    color: 'rgb(255, 255, 255)'
                },
            }],
          xAxes: [{
                ticks: {
                    color: 'rgb(255, 255, 255)'
                },
            }]
        } ,
          plugins: {
              tooltip:{

              },
            legend: {
                display: true,
                labels: {
                    color: 'rgb(255, 255, 255)'
                }
            }
        }
      }
    });

    const myChart2 = new Chart(ctx2, {
      type: 'bar',
      data: {
        labels: dataTemps.dates,
        datasets: dataTemps.all_data
      },
      options: {}
    });

    const myChart3 = new Chart(ctx3, {
      type: 'pie',
      data: {
        labels: dataTemps.RFID,
        datasets: dataTemps.all_date2
      },
      options: {}
    });

    const myChart4 = new Chart(ctx4, {
      type: 'doughnut',
      data: {
        labels: dataTemps.RFID,
        datasets: dataTemps.all_date2
      },
      options: {}
    });

    const myChart5 = new Chart(ctx5, {
      type: 'radar',
      data: {
        labels: dataTemps.dates,
        datasets: dataTemps.all_data
      },
      options: {}
    });

    const myChart6 = new Chart(ctx6, {
      type: 'polarArea',
      data: {
        labels: dataTemps.RFID,
        datasets: dataTemps.all_date2
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: 'top',
          },
          title: {
            display: true,
            text: 'Chart.js Bubble Chart'
          }
        }
      },
    });



  }


  async function getData() {

    const response = await fetch('/media/data/AnimalWeights_3.csv');
    const data = await response.text();

    //console.log(single);

    const rows = data.split('\n');
    console.log(rows);

    const dates = data.split('\n').slice(0,1)[0].split(',').slice(2);
    console.log(dates);

    const RFID = [];

    var i=1;
    var weights = [];
    const all_data = [];


    const color_palette_1 = [
        "rgba(255,99,132,1)",
        "rgb(77,4,255, 1)",
        "rgba(255,0,132,1)",
        "rgba(255,99,0,1)",
        "rgba(255,0,0,1)",
        "rgba(255,255,0,1)",
        "rgba(150,99,132,1)",
        "rgba(60,150,132,1)",
        "rgba(10,20,132,1)",
        "rgba(100,99,50,1)",
    ];


    const color_palette_2 = [
        "rgba(255,99,132,0.2)",
        "rgba(77,4,255, 0.2)",
        "rgba(255,0,132,0.2)",
        "rgba(255,99,0,0.2)",
        "rgba(255,0,0,0.2)",
        "rgba(255,255,0,0.2)",
        "rgba(150,99,132,0.2)",
        "rgba(60,150,132,0.2)",
        "rgba(10,20,132,0.2)",
        "rgba(100,99,50,0.2)",
    ];

      const color_palette_4 = [
        "rgba(255,99,132,0.4)",
        "rgba(77,4,255, 0.4)",
        "rgba(255,0,132,0.4)",
        "rgba(255,99,0,0.4)",
        "rgba(255,0,0,0.4)",
        "rgba(255,255,0,0.4)",
        "rgba(150,99,132,0.4)",
        "rgba(60,150,132,0.4)",
        "rgba(10,20,132,0.4)",
        "rgba(100,99,50,0.4)",
    ];





    for(i=1; i<rows.length; i++){
        const x = {
            label: '',
            data: '',
            color: 'rgb(255, 255, 255)',
            fill: false,
            borderColor: 'DodgerBlue',
            backgroundColor: 'DodgerBlue',
            hoverBackgroundColor: "rgba(255,99,132,0.4)",
            hoverBorderColor: "rgba(255,99,132,1)",
            borderWidth: 2,
            hoverOffset: 4,

          };

        weights[i-1] = rows[i].split(',').slice(1);

        RFID[i-1] = weights[i-1][0];

        x.label = RFID[i-1];
        x.data = weights[i-1].slice(1);
        x.borderColor = color_palette_1[ (i-1)%color_palette_1.length ];
        x.backgroundColor = color_palette_2[ (i-1)%color_palette_2.length ];
        x.hoverBorderColor = color_palette_1[ (i-1)%color_palette_1.length ];
        x.hoverBackgroundColor = color_palette_4[ (i-1)%color_palette_4.length ];

        all_data[i-1] = x;
    }
    console.log(weights);
    console.log(RFID);



    const  weights_per_date = [];
    const rows2 = data.split('\n').slice(1);

    const n_rows = weights.length;
    const n_col = dates.length;

    var row = 0;
    var col = 0;

    for(col=1; col<n_col+1; col++){
        const w = [];
        for(row=0; row<n_rows; row++){
            w[row] = weights[row][col];
        }
        weights_per_date[col-1] = w;
    }

    console.log(weights_per_date);
    console.log(RFID);
    console.log(dates);
    console.log(weights);

    const all_date2 = [];

    for(i=0; i<dates.length; i++){
        const x = {
            label: dates[i],
            data: weights_per_date[i],
            fill: false,
            borderColor: color_palette_1,
            backgroundColor: color_palette_2,
            hoverBackgroundColor: color_palette_4,
            hoverBorderColor: color_palette_1,
            borderWidth: 2,
            hoverOffset: 10
          };

        all_date2[i] = x;
    }


    return { dates, all_data, RFID, all_date2, weights};
  }


