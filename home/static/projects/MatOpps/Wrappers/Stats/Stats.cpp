#include <iostream>
#include "Stats.h"

using namespace std;

namespace stats {
    Regress::Regress(){}
    Regress::Regress(vector<double> v_arr, int size){      
        this->main_arr = v_arr;
        this->size=size; 
    }
    Regress::~Regress(){}

    vector<double> Regress::sample(){
        return this->main_arr;
    }

    double Regress::mean(){
        int i=0;
        int counter=0;
        double sum=0;

        for(i;i<this->size;i++){
            sum+=this->main_arr[i];
            counter++;
        }
        return sum/counter;
    }

    MODE Regress::mode(){
        int i=0;
        int j=0;
        for(i=0;i<this->size;i++){
            int counter=0;
            for(j=0;j<size;j++)
            {
                if(this->main_arr[i]==this->main_arr[j])
                {
                    counter++;
                }
            }
            this->arrDict.insert(pair<double, int>(this->main_arr[i], counter));
            //cout<<tmpi<<"=>"<<counter<<endl;
        }
        map<double, int>::iterator it=this->arrDict.begin();

        MODE mode;
        mode.number=this->arrDict.begin()->first;
        mode.count=this->arrDict.begin()->second;

        for(it; it!=this->arrDict.end();++it)
            if (it->second>=mode.count){
                mode.number=it->first;
                mode.count=it->second;
            }     

        return mode;  
    }
 
    double Regress::min(){
        double _min=this->main_arr[0];
        for(int i=0;i<this->size;i++)
        {
            if (main_arr[i]<=_min)
                _min=this->main_arr[i];
        }
        return _min;
    }

    double Regress::max(){ 
        double _max=this->main_arr[0];
        for(int i=0;i<this->size;i++)
        {
            if (main_arr[i]>=_max)
                _max=this->main_arr[i];
        }
        return _max;
    }

    double Regress::SD()
    {
        double _mean=this->mean();
        double nVar=0;
        double sd;
        for(int i=0;i<this->size;i++)
        {
            nVar+=pow((this->main_arr[i]-_mean), 2);
        }
        sd=sqrt((nVar)/(this->size-1));
        return sd;
    }

    double Regress::Var(){
        return pow(this->SD(), 2);
    }
}
