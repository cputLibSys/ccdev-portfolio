#ifndef STATS_H
#define STATS_H
#include <map>
#include <cmath>
#include <vector>

using namespace std;

namespace stats {
    struct MODE {
        double number;
        int count;
    };
    class Regress{
        public:
            vector<double> main_arr;
            int size;
            map <double, int> arrDict;
            Regress();
            Regress(vector<double> v_arr, int size);
            ~Regress();
            
            vector<double> sample();
            double mean();
            MODE mode();
            double min();
            double max(); 
            double SD(); 
            double Var();  
    };
}

#endif