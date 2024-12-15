import { Component, ViewChild } from '@angular/core';
import { $ } from 'protractor';
import { TouchSequence } from 'selenium-webdriver';
import { StatDataService } from './stat-data.service';
import {Chart, registerables} from "./Chart";
import annotationPlugin from './chartjs-plugin-annotation.min';
import * as XLSX from 'xlsx';
import { empty } from 'rxjs';
import { deepStrictEqual } from 'assert';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  title = 'InterStats';
  mathml=""; 

  public xV="";
  public yV=""; 
  public pick="Normal";

  public ZChart: any = null; 
  public z_leftL=Math.round((-3.1 + Number.EPSILON) * 1000) / 1000;
  public z_rightL=Math.round((0 + Number.EPSILON) * 1000) / 1000;
  public Chart: any=null;

  constructor(private statService: StatDataService){

  }

  public Data = {
    sampN:0,
    popM: 0,
    popSD: 0,
    sampM: 0,
    sigL: 0,
    Ops: {

    }
  };
 

  public s_zValues=[];
  public s_yValues=[];
  
  public CusData: any = {
    xValues: new Float64Array([]),
    yValues:new Float64Array([]),
    mean:new Float64Array([0, 0]),
    mode: new Float64Array([0, 0]),
    range: new Float64Array([0, 0]),
    sd: new Float64Array([0, 0]),
    Ops:{
      mean: (data)=>{
        var _sum=0, y_sum=0;
        for(var i=0;i<data.length; i++)
          _sum+=data[i];
  

        return data.length<1?0:(_sum/data.length);
      }, 
      mode: ()=>{
        var tmp_vals=this.CusData.xValues.sort();
        var count=1;
        var max=[this.CusData.xValues[0],count];
        for(var i=1;i<this.CusData.xValues.length;i++)
        {
          if(max[0]==tmp_vals[i])
          {
            count++;
            max[1]=count;
          }
          else{
            if(count>max[1])
            {
              max[0]=tmp_vals[i];
              max[1]=count;
            }
            count=1;
          }
        }
        this.CusData.mode[0]=max[0];
      },
      range: (data)=>{
        var tmp_data=data.sort();
        return Math.max(...tmp_data)-Math.min(...tmp_data);
      },
      sd: (data, X)=>{ 
        var tmp_data=0;
        for(var i=0;i<data.length; i++){
          tmp_data+=Math.pow(X-data[i], 2);
        }
        return Math.sqrt(tmp_data/data.length);
      }
    }
  }


  public importFile(event){
    this.statService.readFile(event);

  }

  public z_change(){
  
    var accReg_1, rejReg, accReg_2;
    var _self=this;

    this.genZData(0, 1, 0, this.z_leftL, this.z_rightL).then(function(data){
      accReg_1=data[0];
      rejReg=data[1];
      accReg_2=data[2];

      _self.ZChart.data.datasets=[];

      _self.ZChart.data.datasets.push({
        backgroundColor: "rgba(0,0,255,1.0)",
        data: accReg_1
      });
      _self.ZChart.data.datasets.push({
        backgroundColor: "rgba(0,0,255,1.0)",
        data:rejReg
      });
      _self.ZChart.data.datasets.push({
        backgroundColor: "rgba(0,0,255,1.0)",
        data: accReg_2
      });

      _self.ZChart.update(); 
    });
    
  }


  public genZData(X, popSD, popMean, ll, rl){
    var _self=this;
    var accReg_1, rejReg, accReg_2;
      
    return new Promise<any>(function(resolve, reject){
      
      var z_a=-4;
      var z_b=4;
      _self.s_zValues=[];
      _self.s_yValues=[];

      
      let myPromise = new Promise(function(resolve, reject) {
        // "Producing Code" (May take some time)
       
          for(z_a;z_a<=z_b;z_a+=1/100){
            _self.s_zValues.push(Math.round((z_a + Number.EPSILON) * 100) / 100 );
            _self.s_yValues.push((1/Math.sqrt(2*Math.PI*popSD))*Math.pow(Math.E, -0.5*(Math.pow((z_a-0)/(1), 2)) ));
          }
          
          resolve([_self.s_zValues, _self.s_yValues]); // when successful
          reject();  // when error
      });

      myPromise.then(function (data){
        //alert(data[0].length);
        accReg_1=_self.s_yValues.slice(0, data[0].indexOf(_self.z_leftL)+1);  
        rejReg=Array(accReg_1.length-1).fill('-').concat(_self.s_yValues.slice(_self.s_zValues.indexOf(_self.z_leftL), _self.s_zValues.indexOf(_self.z_rightL)+1));
        accReg_2=Array(rejReg.length-1).fill('-').concat(_self.s_yValues.slice(_self.s_zValues.indexOf(_self.z_rightL), _self.s_yValues.length));
      }, function (err){
        alert(err);
      }).then(function(){
        resolve([accReg_1, rejReg, accReg_2]);
        reject();
      })
    

    });
    //console.log(this.s_zValues);
    /*
    var z=ll;
    var z_a=-4;
    var z_b=rl;

    this.s_zValues=[[], [], []];
    this.s_yValues=[[], [], []];

    for(z_a;z_a<=ll;z_a+=(1/12)){
      this.s_zValues[0].push(Math.round((z_a + Number.EPSILON) * 10000) / 10000);
      this.s_yValues[0].push((1/Math.sqrt(2*Math.PI*popSD))*Math.pow(Math.E, -0.5*(Math.pow((z_a-0)/(1), 2)) ));
    }
  
  
    for(z;z<=rl;z+=(1/12)){
      this.s_zValues[1].push(Math.round((z + Number.EPSILON) * 10000) / 10000);
      this.s_yValues[1].push((1/Math.sqrt(2*Math.PI*popSD))*Math.pow(Math.E, -0.5*(Math.pow((z-0)/(1), 2)) ));
    } 
    
    for(z_b;z_b<=4;z_b+=(1/12)){
      this.s_zValues[2].push(Math.round((z_b + Number.EPSILON) * 10000) / 10000);
      this.s_yValues[2].push((1/Math.sqrt(2*Math.PI*popSD))*Math.pow(Math.E, -0.5*(Math.pow((z_b-0)/(1), 2)) ));
    }
   */
  }

  public Distributions = { 
    
    Ops: {
      factorial:(n)=>{
        if (n==1)
          return 1;
        else
          return n*this.Distributions.Ops.factorial(n-1);
      }
    },

    binomial:(n, x, p)=>{
      var n_x=(this.Distributions.Ops.factorial(n))/(this.Distributions.Ops.factorial(x)*this.Distributions.Ops.factorial(n-x));
      var q=1-p;
      return n_x*Math.pow(p, x)*Math.pow(q, n-x);
    },
    poisson:()=>{

    },
    normal: {
      params: [],
      conditions: [],
      func: (u, sd) =>{

        var accReg_1, rejReg, accReg_2;

        var _self=this;

        var prom = new Promise((resolve, reject)=>{

          _self.CusData.xValues=[];
          _self.CusData.yValues=[];
          
          /*
          for(var i=0; i<5;i+=1/30){
            if(i>0){
              this.CusData.xValues.push(u-(i*sd));
              this.CusData.xValues.push(u+(i*sd));
            }else{
              this.CusData.xValues.push(u);
            }
          }

          for(var i=0; i<this.CusData.xValues.length; i++){
            this.CusData.yValues.push((1/Math.sqrt(2*Math.PI*sd))*Math.pow(Math.E, -0.5*(Math.pow((this.CusData.xValues[i]-u)/sd, 2)) ));
          }*/

          let myPromise = new Promise((resolve, reject) => {
            var z_alpha=-4;
            for(z_alpha;z_alpha<=4;z_alpha+=(1/30)){
              var xVal=u-Math.round((z_alpha*sd + Number.EPSILON) * 10000) / 10000;
              _self.CusData.xValues.push(xVal);
              _self.CusData.yValues.push((1/Math.sqrt(2*Math.PI*sd))*Math.pow(Math.E, -0.5*(Math.pow((xVal-u)/(sd), 2)) ));
            } 
            
            resolve(0);
            reject();
          });

          myPromise.then(() => {
            
            accReg_1=_self.CusData.yValues.slice(0, _self.CusData.xValues.indexOf(_self.z_leftL)+1); 
            alert(accReg_1.length);
            rejReg=Array(accReg_1.length-1).fill('-').concat(_self.CusData.yValues.slice(_self.CusData.xValues.indexOf(_self.z_leftL), _self.CusData.xValues.indexOf(_self.z_rightL)));
            accReg_2=Array(rejReg.length-1).fill('-').concat(_self.CusData.yValues.slice(_self.CusData.xValues.indexOf(_self.z_rightL), _self.CusData.yValues.length));
            
          }, (err)=>{
            alert(err);
          }).then(()=>{
            resolve([accReg_1, rejReg, accReg_2]);
            reject();
          });

          

        });
        prom.then(function(data){

          var d1=data[0];
          var d2=data[1];
          var d3=data[2];

          _self.Chart = new Chart("cusChart", {
                type: "line",
                data: {
                  labels:this.CusData.xValues,
                  datasets: [
                    {
                    fill: false,
                    lineTension: 0,
                    backgroundColor: "#66a3ff",
                    borderColor: "rgba(0,0,255,0.1)",
                    color:"rgba(100,0,255,0.1)",
                    label: "Distribution of X~("+this.Distributions.normal.params[0]+", "+this.Distributions.normal.params[1]+")",
                    data: d1
                  },{
                    fill: false,
                    lineTension: 0,
                    backgroundColor: "#66a3ff",
                    borderColor: "rgba(0,0,255,0.1)",
                    color:"rgba(100,0,255,0.1)",
                    label: "",
                    data: d2             
                  },{
                    fill: false,
                    lineTension: 0,
                    backgroundColor: "#66a3ff",
                    borderColor: "rgba(0,0,255,0.1)",
                    color:"rgba(100,0,255,0.1)",
                    label: "",
                    data: d3
                  }
                ]
                },
                options: {
              
                  scales: {
                    xAxes: {
                      ticks:{
                        min: Math.min(...this.CusData.xValues),
                        max: Math.max(...this.CusData.xValues)
                      },
                      scaleLabel: {
                        display: true,
                        fontSize: 18,
                        labelString: "X"
                      }
                    },
                    yAxes: [{
                      ticks:{
                        min: Math.min(...this.CusData.yValues),
                        max: Math.max(...this.CusData.yValues)
                      },
                      scaleLabel: {
                        display: true,
                        labelString: 'Probability' 
                      }
                    }],
                  title: {
                      display: true,
                  },        
                },
              }
          });
        });
      }
    },
    exponential:()=>{

    },
    studentsT: (X, popSD, popMean,n, sigL)=>{ 

    },

  }

  public updateData(){

    this.CusData.xValues.splice(0);
    this.CusData.yValues.splice(0);

    this.CusData.xValues=new Float64Array(this.xV.split(",").map(Number));
    this.CusData.yValues=new Float64Array(this.yV.split(",").map(Number));
    var plotCheck=this.CusData.xValues.length-this.CusData.yValues.length;

    var plot = ()=>{
      new Chart("cusChart", {
        type: "line",
        data: {
          labels:this.CusData.xValues,
          datasets: [{
            fill: false,
            lineTension: 0,
            backgroundColor: "rgba(0,0,255,1.0)",
            borderColor: "rgba(0,0,255,0.1)",
            color:"rgba(100,0,255,0.1)",
            data: this.CusData.yValues
          }]
        }
      });
    }
    
    if(plotCheck==0){
      plot();
    }
    else if(plotCheck>0){
      plot();
    }else{
      
    }   
  }

  public bestFit(){
    var b1, b0;
    var _num=0,_den=0;

    for(var i=0;i<_num;i++){
      _num+=(this.CusData.xValues[i]-this.CusData.mean[0])*(this.CusData.yValues[i]-this.CusData.mean[1]);
      _den+=Math.pow((this.CusData.xValues[i]-this.CusData.mean[0]), 1);
    }
    b1=_num/_den;
    b0=this.CusData.mean[1]-this.CusData.mean[0]*b1;
  }

  ngAfterViewInit(){
 
    var accReg_1, rejReg, accReg_2;
    var _self=this;

    this.genZData(0, 1, 0, this.z_leftL, this.z_rightL).then(function(data){
      accReg_1=data[0];
      rejReg=data[1];
      accReg_2=data[2];
    
      _self.ZChart = new Chart("myChart", {
        type: "line",
        data: {
          labels: _self.s_zValues,
          datasets: [{
            fill: true,
            label:"Acceptance Region",
            backgroundColor: "rgba(0,0,255,1.0)",
            borderColor: "rgba(0,0,255,0.1)",
            data:accReg_1
          },
          {
            fill: true,
            label:"Rejection region",
            backgroundColor: "rgba(255,51,51,1.0)",
            borderColor: "rgba(0,0,255,0.1)",
            data: rejReg
          },
          {
            fill: true,
            label:"Acceptance region",
            backgroundColor: "rgba(0,0,255,1.0)",
            borderColor: "rgba(0,0,255,0.1)",
            data: accReg_2
          }
        ],
        },
  
        options: {
          scales: {
            xAxes: {
              ticks:{
                min: Math.min(..._self.s_zValues),
                max: Math.max(..._self.s_zValues)
              },
              scaleLabel: {
                display: true,
                fontSize: 18,
                labelString: "Make long enough to truncate"
              }
            },
            yAxes: [{
              ticks:{
                beginAtZero:true
              },
              scaleLabel: {
                display: true,
                labelString: 'Probability'
              }
            }],
          title: {
              display: true,
           },        
        },
      }
      });
  
    },
    function(err){

    });
    //this.genCusData(20, 1, 10, 20, 0);
    //console.log(this.s_zValues[0].concat(this.s_yValues[1]).concat(this.s_yValues[2]));
   
  
    var arr=[];
    function genArr(){ for(var i=0;i<=50;i++){arr.push(i)} return arr; }
    genArr();

    this.Chart = new Chart("cusChart", {
      type: "line", 
      data: { 
        labels:arr,
        datasets: [{
          borderColor: "rgba(0,0,255,0.1)",
          data:[]
        }]
      },
      options: {
        legend: {display: true},
        scales: {
          xAxes: [{
            ticks:{
              min: Math.min(...arr),  
              max: Math.max(...arr)
            },
            scaleLabel: {
              display: true,
              labelString: 'X'
            }
          }],
          yAxes: [{
            ticks:{
              min: Math.min(...arr),
              max: Math.max(...arr)+0.1
            },
            scaleLabel: {
              display: true,
              labelString: 'Y'
            }
          }],
        },
        title: {
            display: true,
            text: 'Y as a Function of X'
        }
      }
    });

  }
}
