import { Injectable } from '@angular/core';
import { Observable, Subject } from 'rxjs';
import * as XLSX from 'xlsx';

@Injectable({
  providedIn: 'root'
})
export class StatDataService {
  file:File;
  arrayBuffer:any;
  filelist:any;
  DATA = new Subject();

  constructor() { 

    this.DATA.subscribe(data => {
      console.log(data);
    }); 

  }
  
  public readFile(event){
    this.file=event.target.files[0];
    let fileReader=new FileReader();
    fileReader.readAsArrayBuffer(this.file);
    fileReader.onload = (e)=>{
      this.arrayBuffer=fileReader.result;
      var data = new Uint8Array(this.arrayBuffer);    
      var b_arr = new Array();    
      
      for(var i = 0; i != data.length; ++i) b_arr[i] = String.fromCharCode(data[i]);    

      var bstr = b_arr.join(""); 
      var workbook = XLSX.read(bstr, {type:"binary"});    
      var sheet_name = workbook.SheetNames[0];    
      var worksheet = workbook.Sheets[sheet_name];  
      this.DATA.next(XLSX.utils.sheet_to_json(worksheet,{raw:true}));
    }
  }
}
