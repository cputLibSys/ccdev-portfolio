extern crate pyo3;

use pyo3::prelude::*;
use pyo3::types::*;
use pyo3::{Python, PyErr};
use pyo3::exceptions::PyTypeError;

use std::f32::consts::*;
use std::fmt;
use std::collections::*;
/// Formats the sum of two numbers as string.
#[pyclass]
#[derive(Clone)]
pub struct Matrix {
    #[pyo3(get, set)]
    elements: Vec<Vec<f32>>,
}


impl fmt::Display for Matrix{
    fn fmt(&self, f: &mut fmt::Formatter)->fmt::Result {
        for row in self.elements.iter(){
            write!(f, "{:?}\n", row);
        }
        Ok(())
    }
}


#[pyclass]
#[derive(Copy, Clone)]
pub struct Vector{
    x_1: f32,
    x_2: f32,
    x_3: f32,
}

#[pymethods]
impl Vector {
    #[new]
    fn new(x_1: f32, x_2:f32, x_3:f32) ->Self{  
        Self{x_1: x_1, x_2: x_2, x_3: x_3}
    }

    fn __str__(&self) -> PyResult<String>   {
        Ok(format!("<{}, {}, {}>", self.x_1, self.x_2, self.x_3))
    }

    fn __repr__(&self) -> Vector{
        *self
    }

    fn len(&self)->f32{
        (self.x_1.powi(2)+self.x_2.powi(2)+self.x_3.powi(2)).sqrt()
    }

    fn scale(&mut self, c: f32)-> Vector{
        self.x_1*=c;
        self.x_2*=c;
        self.x_3*=c;

        return *self
    }

}

#[pymethods]
impl Matrix {
    #[new]
    fn new(matrix: Vec<Vec<f32>>)-> Self {
        Self{elements: matrix}
    }

    fn __str__(&self) -> PyResult<String>   {
        let mut s: String="".to_string();
        for row in self.elements.iter(){
            s.push_str(&format!("{:?}\n", row).to_string());
        }
        Ok((s))
    }

    //fn det(){}
}

#[pymodule]
fn init_vecops(_py: Python, m: &PyModule) -> PyResult<()>{
    #[pyfn(m)]
    #[pyo3(signature = (*vectors, opp='+'))]
    fn add(vectors: &PyTuple, opp: char) -> Vector{
        let _vectors=vectors.extract::<Vec<Vector>>().unwrap();
        let vec_res= &mut _vectors[0].clone();

        for vector in _vectors[1..].iter(){
            if opp=='+' {
                vec_res.x_1+=vector.x_1;
                vec_res.x_2+=vector.x_2;
                vec_res.x_3+=vector.x_3;
            }else{
                vec_res.x_1-=vector.x_1;
                vec_res.x_2-=vector.x_2;
                vec_res.x_3-=vector.x_3;
            }

        }

        *vec_res
    }
    #[pyfn(m)]
    #[pyo3(signature = (*vectors))]
    fn sub(vectors: &PyTuple) -> Vector{ add(vectors) };

    fn dot_prod(v1, v2){

    }

    Ok(())
}

#[pymodule]
fn init_matops(_py: Python, m: &PyModule) -> PyResult<()>{

    #[pyfn(m)]
    fn matToHash(matrix: Matrix) -> HashMap<&str, f32>{
        let mut mat_map: HashMap<&str, f32>=HashMap::new();
        for i in 0...matrix.elements.len(){
            for k in 0..matrix.elements[i].len(){
                mat_hash.insert(format!("({},{})", i, k), matrix.elements[i][k]);
            }
        }
        mat_map
    }

    #[pyfn(m)]
    fn inverse(matrix: Matrix)-> Matrix{
        let n, m=matrix.elements.len(), matrix.elements[0].len();
        let hashed_mat: HashMap<&str, f32>=matToHash(matrix);

        if n==m{
            for i in 0..
        }else{

        }
    }
    #[pyfn(m)]
    fn transpose(matrix: Matrix)-> Matrix{
        let mut new_mat: Matrix=Matrix::new(vec![]);

        for row in matrix.elements.iter(){
            let mut c=0;
            new_mat.elements.push(vec![]);
            for el in row.iter(){
                new_mat.elements[c].push(*el);
                //println!("{:?}", new_mat.elements);
                c+=1;
            }
        }
        new_mat
    }

    #[pyfn(m)]
    fn dot_prod(vec1: Vec<f32>, vec2:Vec<f32>) -> f32{
        let mut prod: f32=0.0;
        for i in 0..vec1.len(){
            prod+=vec1[i]*vec2[i];
        }

        prod
    }

    #[pyfn(m)]
    #[pyo3(signature = (*matrices, opp='+'))]
    fn add(matrices: &PyTuple, opp: char) -> Matrix{
        let _matrices=matrices.extract::<Vec<Matrix>>().unwrap();
        let matrix_prod = &mut _matrices.clone()[0];

        for matrix in _matrices[1..].iter(){
            let mut new_mat:Vec<Vec<f32>>=vec![];
            for i in 0..matrix_prod.elements.len(){
                new_mat.push(vec![]);
                for k in 0..matrix_prod.elements[i].len(){
                    if opp=='+'{
                        new_mat[i].push(matrix_prod.elements[i][k]+matrix.elements[i][k]);
                    }else{
                        new_mat[i].push(matrix_prod.elements[i][k]-matrix.elements[i][k]);
                    }
                }
            }
            matrix_prod.elements=new_mat;
        } 

        matrix_prod.clone()
    }

    #[pyfn(m)]
    #[pyo3(signature = (*matrices))]
    fn sub(matrices: &PyTuple)->Matrix{
        add(matrices, '-')
    }

    #[pyfn(m)]
    #[pyo3(signature = (*matrices))]
    fn multiply(matrices: &PyTuple) -> Matrix{
        let _matrices=matrices.extract::<Vec<Matrix>>().unwrap();
        let matrix_prod = &mut _matrices.clone()[0];
        
        for matrix in _matrices[1..].iter(){
            let _next=transpose(matrix.clone());
            if matrix_prod.elements[0].len() ==_next.elements[0].len(){
                let mut new_mat:Vec<Vec<f32>>=vec![];
                let mut c=0;
                for row in matrix_prod.elements.iter(){ 
                    new_mat.push(vec![]);         
                    for col in _next.elements.iter(){                   
                        new_mat[c].push(dot_prod(row.to_vec(), col.to_vec()))
                    }
                    c+=1;
                }
                matrix_prod.elements=new_mat;
            }else{
                println!("Error");
            }
        }

        matrix_prod.clone()
    }
    Ok(())
}
/// A Python module implemented in Rust.
#[pymodule]
fn linear_algebra(_py: Python, m: &PyModule) -> PyResult<()> {
    let matops_mod=PyModule::new(_py, "mat_ops")?;
    init_matops(_py, matops_mod)?;
    m.add_submodule(matops_mod)?;

    let vecops_mod=PyModule::new(_py, "vec_ops")?;
    init_vecops(_py, vecops_mod)?;
    m.add_submodule(vecops_mod)?;

    m.add_class::<Matrix>()?;
    m.add_class::<Vector>()?;
    Ok(())
}