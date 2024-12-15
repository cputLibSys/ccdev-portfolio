#include <iostream>
#include "Complex.h"

namespace ComplexOps{
    ComplexMath::ComplexMath(){}
    ComplexMath::~ComplexMath(){}

    vector<double> ComplexMath::structToVector(ComplexN num){
        vector<double> new_num;
        new_num[0]=num.real_part;
        new_num[1]=num.imag_part;
        return new_num;
    }

    int  ComplexMath::setComplexN(vector<double> cn){
        static int c_nums_count=0; 
        ComplexN new_cn;
        new_cn.real_part=cn[0];
        new_cn.imag_part=cn[1];
        this->c_nums.push_back(new_cn);

        for (int i=0;i<2;i++)
            continue;
            //cout<<cn[i]<<end
        c_nums_count++;
        return c_nums_count;
    }

    ComplexN ComplexMath::SUM(vector<int> range, int r){
        ComplexN res;
        if (r==0)
        {
            int i=range[0];
            int j=range[1];
            res.real_part=(this->c_nums[i].real_part+c_nums[j].real_part);
            res.imag_part=(this->c_nums[i].imag_part+c_nums[j].imag_part);
        }
        else
        {
            int trp=0;
            int timp=0;
            for(int i=0;i<range.size();i++)
            {
                int _i=range[i];
                trp+=this->c_nums[_i].real_part;  
                timp+=this->c_nums[_i].imag_part;
            }
            res.real_part=trp;
            res.imag_part=timp;
        }
        return res;
    }

    ComplexN ComplexMath::PRODUCT(int i, int j){
        ComplexN res;
        res.real_part=(this->c_nums[i].real_part*this->c_nums[j].real_part)-(this->c_nums[i].imag_part*this->c_nums[j].imag_part);
        res.imag_part=(this->c_nums[i].real_part*this->c_nums[j].imag_part)+(this->c_nums[j].real_part*this->c_nums[i].imag_part);
        return res;
    }

    ComplexN ComplexMath::RecursiveProd(vector<int> range)
    {   
        ComplexN prod;
        prod.real_part=this->c_nums[range[0]].real_part;
        prod.imag_part=this->c_nums[range[0]].imag_part;
        for(int i=1;i<range.size();i++){
            int j=range[i];
            prod.real_part=(this->c_nums[j].real_part*prod.real_part)-(c_nums[j].imag_part*prod.imag_part);
            prod.imag_part=(this->c_nums[j].real_part*prod.imag_part)+(prod.real_part*this->c_nums[j].imag_part);
        }
        return prod;
    }

    ComplexN ComplexMath::DIV(int i, int j)
    {
        ComplexN cn_num, cn_den, conj, new_cn;
        
        conj.real_part=this->c_nums[j].real_part;
        conj.imag_part=-1*this->c_nums[j].imag_part;
        
        int x=this->c_nums.size()-1;
        this->c_nums[x]=conj;

        cn_den=this->PRODUCT(j, x);
        cn_num=this->PRODUCT(i, x);

        cout<<cn_den.real_part<<endl;
        
        new_cn.real_part=cn_num.real_part/cn_den.real_part;
        new_cn.imag_part=cn_num.imag_part/cn_den.imag_part;

        return new_cn;
    }

    ComplexN ComplexMath::POW(int i, int n){
        ComplexN cn = c_nums[i];
        ComplexN res;
        
        double res_mag = pow(cn.modulus(), n);
        double res_arg = cn.argument()*cn.deg_to_rad;
        cout<<cn.argument()<<endl;
        double rp = cos(res_arg*n);
        double imp = sin(res_arg*n);

        res.real_part=res_mag*rp;
        res.imag_part=res_mag*imp;

        return res;
    }
}