class calc
{
    int su1, su2;
public :
    int add(int a, int b);
    int min(int a, int b);
    int mul(int a, int b);
    double div(int a, int b);
};
 
int calc::add(int a, int b)
{
    return a + b;
}
 
int calc::min(int a, int b)
{
    return a - b;
}
 
int calc::mul(int a, int b)
{
    return a * b;
}
 
double calc::div(int a, int b)
{
    return (double)a / (double)b;
}
 
void main()
{
    calc cal;
    cout << "cal.add(10, 19) = " << cal.add(10, 19) << endl;
    cout << "cal.min(21, 5) = " << cal.min(21, 5) << endl;
    cout << "cal.mul(4, 12) = " << cal.mul(4, 12) << endl;
    cout << "cal.div(7, 2) = " << cal.div(7, 2) << endl;
}
