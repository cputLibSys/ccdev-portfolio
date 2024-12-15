#ifndef COMPLEX_H
#define COMPLEX_H

#include <cmath>
#include <vector>
#include <string> 

#define PI 3.141592653589793238462643

using namespace std;

namespace ComplexOps{
    struct ComplexN{
        double real_part;
        double imag_part;
        double rad_to_deg=180.0/PI;
        double deg_to_rad=PI/180.0;

        double modulus(){
            return sqrt(pow(real_part,2)+pow(imag_part, 2));
        }
        double argument(){
            if (imag_part==0)
                return 0.0;
            else
                return atan(imag_part/real_part)*rad_to_deg;
        }
    };

    class ComplexMath{
        public:
            typedef ComplexN CN;
            vector<CN> c_nums;
            ComplexMath();
            ~ComplexMath();
            vector<double> structToVector(ComplexN num);
            int setComplexN(vector<double> cn);
            ComplexN SUM(vector<int> range,int r);
            ComplexN PRODUCT(int i, int j);
            ComplexN RecursiveProd(vector<int> range);
            ComplexN DIV(int i, int j);
            ComplexN POW(int i, int n);
    };
}

#endif