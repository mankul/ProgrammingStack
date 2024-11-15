#include<iostream>
#include<vector>

using namespace std;

void sumMatrices(vector< vector<int> > & mat1, vector< vector<int> > & mat2, int m1, int n1, int m2, int n2){
    /*
	for(auto out_iter = mat1.begin(); out_iter != mat1.end(); out_iter++){
		for(auto inner_iter = (*out_iter).begin(); inner_iter != (*out_iter).end(); inner_iter++){
            cout<<*inner_iter<<endl;
        }
	}
    */
    if (m1 != m2 || n1 != n2)
        return;
    for(int i = 0; i < m1; i++)
    {
        for(int j = 0 ; j < n1; j++)
        {
            cout<<mat1[i][j] + mat2[i][j]<<"\t";
        }
	cout<<endl;
    }
}


int main(){
    int m=25, n=25;
    
	//vector< vector<int> > matrix1;// = {{0},{1},{2}};
	//vector< vector<int> > matrix2;// = {{0},{1},{2}};
	vector< vector<int> > matrix1(m, vector<int>(n,1));// = {{0},{1},{2}};
	vector< vector<int> > matrix2(m, vector<int>(n,4));// = {{0},{1},{2}};
    for(int i = 0; i< m; i++){
        //vector<int> vec1;
        //vector<int> vec2;
        for(int j = 0 ; j < n; j++)
            {
                matrix1[i][j] += i + j;
                
                //vec1.push_back(i + j + 10);
                //vec2.push_back(i * j * 2);
            }
        //matrix1.push_back(vec1);
        //matrix2.push_back(vec2);
    }

    sumMatrices(matrix1, matrix2, m, n, m , n);
	return 0;
}
