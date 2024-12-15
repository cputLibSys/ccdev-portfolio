use pyo3::prelude::*;
use pyo3::types::*;
use std::f32::consts::*;
/// Formats the sum of two numbers as string.

use serde::{Serialize, Deserialize};

const rad_to_deg: f32=180.0/PI;
const deg_to_rad: f32=PI/180.0;

#[pyclass]
#[derive(Copy, Clone)]
pub struct CPLX_NUM {
    #[pyo3(get, set)]
    real_part: f32,
    #[pyo3(get, set)]
    img_part: f32,
}


#[pymethods]
impl CPLX_NUM {
    
    #[new]
    fn new(real_part: f32, img_part: f32) -> Self {
        println!("real: {}, img:{}", real_part, img_part);
        Self{real_part: real_part, img_part:img_part}
    }

    fn __str__(&self)->PyResult<()>{
        Ok(format!("{}{}{}", self.real_part, self.img_part>0?"+":"-", self.img_part))
    }

    fn modulus(&self)-> f32{
        (self.real_part.powi(2)+self.img_part.powi(2)).sqrt()
    }

    fn argument(&self)->f32{
        if self.img_part==0.0 {
            0.0
        }
        else{
            ((self.img_part/self.real_part)).atan()*rad_to_deg
        }
    }

    #[staticmethod]
    #[pyo3(signature = ( n1, n2, *py_args))]
    fn add(n1: CPLX_NUM, n2: CPLX_NUM, py_args: &PyTuple)-> Vec<f32>{
        let mut real_part=n1.real_part+n2.real_part;
        let mut img_part=n1.img_part+n2.img_part;
        
        if py_args.len()>0{
            for i in 0..py_args.len(){
                let num =py_args.get_item(i).unwrap().extract::<CPLX_NUM>().unwrap();
                real_part+=num.real_part;
                img_part+=num.img_part;
            }
        }
        vec![real_part, img_part]
    }

    #[staticmethod]
    #[pyo3(signature = (*py_args))]
    fn multiply(py_args: &PyTuple)-> Vec<f32>{

        if py_args.len()>0{
            let mut prod = py_args.get_item(0).unwrap().extract::<CPLX_NUM>().unwrap();
            for i in 1..py_args.len(){
                let cplx_num =py_args.get_item(i).unwrap().extract::<CPLX_NUM>().unwrap();
                prod.real_part=prod.modulus()*cplx_num.modulus()*((prod.argument()+cplx_num.argument())*deg_to_rad).cos();
                prod.img_part=prod.modulus()*cplx_num.modulus()*((prod.argument()+cplx_num.argument())*deg_to_rad).sin();
            }

            vec![prod.real_part, prod.img_part]
        }else{
            vec![]
        }
        
    }

    #[staticmethod]
    fn div(cplx_n1:CPLX_NUM, cplx_n2: CPLX_NUM)-> CPLX_NUM{

        let mut cplx_num: CPLX_NUM=CPLX_NUM::new(0.0, 0.0);
        cplx_num.real_part=(cplx_n1.modulus()/cplx_n2.modulus())*((cplx_n1.argument()-cplx_n2.argument())*deg_to_rad).cos();
        cplx_num.img_part=(cplx_n1.modulus()/cplx_n2.modulus())*((cplx_n1.argument()-cplx_n2.argument())*deg_to_rad).sin();
        
        cplx_num
    }
    #[pyo3(signature = (exp=1.0))]
    fn pow(&self, exp: f32)->Vec<f32>{
        let mut _cplx_num=*self;
        _cplx_num.real_part=_cplx_num.modulus().powf(exp)*(_cplx_num.argument()*exp*deg_to_rad).cos();
        _cplx_num.img_part=_cplx_num.modulus().powf(exp)*(_cplx_num.argument()*exp*deg_to_rad).sin();
        
        vec![_cplx_num.real_part, _cplx_num.img_part]
    }
}


#[pymodule]
fn complex(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<CPLX_NUM>()?;
    
    Ok(())
}