use pyo3::prelude::*;
use pyo3::types::*;
use pyo3::{Python, PyErr};
use pyo3::exceptions::PyTypeError;

use std::collections::*;

/// A Python module implemented in Rust.
#[pyclass]
#[derive(Clone)]
struct Points{
    #[pyo3(get, set)]
    x: Vec<f32>,
    #[pyo3(get, set)] 
    y: Vec<f32>,
    #[pyo3(get, set)]
    z: Vec<f32>
}

#[pyclass]
#[derive(Copy, Clone)]
struct MODE{
    #[pyo3(get, set)]
    number: f32,
    #[pyo3(get, set)]
    counter: i32,
}



#[pymethods]
impl Points{
    #[new]
    fn new(x_points: Vec<f32>, y_points: Vec<f32>, z_points: Vec<f32>)-> Self{
        Self { x: x_points, y:y_points, z: z_points }
    }   

}

#[pymodule]
fn stat_ops(_py: Python, m: &PyModule)->PyResult<()>{

    /*#[pyfn(m)]
    fn rec_op(arrs: &PyTuple, rec_opp: fn(Vec<f32>)-> f32)-> PyResult<Vec<f32>>{
        let opp_arr=arrs.extract::<Vec<Vec<f32>>>().unwrap();
        let res_arr: Vec<f32>;
        for vec in opp_arr.iter(){
            res_arr.push(rec_opp(vec.to_vec()));
        }

        Ok(res_arr)
    }*/

    #[pyfn(m)]
    fn avg(arr: Vec<f32>)-> f32{
        let mut _avg: f32=0.0;
        let len: f32=arr.len() as f32;
        for i in 0..arr.len(){
            _avg+=arr[i];
        }

        _avg
    }
    
    #[pyfn(m)]
    fn mode(points: Vec<f32>) -> Vec<MODE>{
        let mut arrDict: HashMap<String, i32>=HashMap::new();

        for i in 0..points.len(){
            let mut counter: i32 =0;
            for j in 0..points.len()
            {
                if(points[i]==points[j])
                {
                    counter+=1;
                }
            }
    
            arrDict.insert(points[i].to_string(), counter);
        }

        let mut mode: Vec<MODE>=vec![MODE {number: 0.0, counter:0}];

        for (_num, counter) in arrDict.iter(){
            let num=_num.parse::<f32>().unwrap();
            if *counter>mode[0].counter && *counter>1 {
                mode[0].number=num;
                mode[0].counter=*counter;
            }else if *counter==mode[0].counter && mode[0].counter!=1{
                
                mode.push(MODE{number: num, counter: *counter});
            }
        }
        
        mode  
    }
 
    #[pyfn(m)]
    fn min(arr: Vec<f32>) -> f32{
        let mut _min: f32=arr[0];
        for i in 0..arr.len()
        {
            if (arr[i]<=_min){
                _min=arr[i];
            }
        }
        _min
    }

    #[pyfn(m)]
    fn max(arr: Vec<f32>) -> f32{ 
        let mut _max: f32=arr[0];
        for i in 0..arr.len()
        {
            if (arr[i]>=_max){
                _max=arr[i];
            }
        }
        _max
    }

    #[pyfn(m)]
    fn SD(arr: Vec<f32>) -> f32
    {
        let  _mean: f32=avg(arr.clone());
        let mut nVar: f32=0.0;
        let mut sd: f32;
        for i in 0..arr.len(){
            nVar+=((arr[i]-_mean)).powi(2);
        }
        sd=((nVar)/(arr.len() as f32)).sqrt();
        sd
    }

    #[pyfn(m)]
    fn Var(arr: Vec<f32>) -> f32{
        (SD(arr)).powi(2)
    }

    Ok(())
}

#[pymodule]
fn stats(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Points>()?;

    let statops_mod=PyModule::new(_py, "STAT_OPS")?;
    stat_ops(_py, statops_mod)?;
    m.add_submodule(statops_mod)?;

    Ok(())
}