#include <bits/stdc++.h>

using namespace std;



int main ()

{

    int t;

    cin >> t;

    

    while (t--)

    {

        int n;

        cin >> n;



        vector<int> v;



        vector<int> answer;



        for (int i=0; i<n; i++)

        {

            int value;

            cin >> value;

            v.push_back(value);

        }



        answer.push_back(v[0]);



        for (int i=1; i<n; i++)

        {

            if (v[i] < v[i-1])

            answer.push_back(v[i]);



            answer.push_back(v[i]);

        }



        cout << answer.size() << endl;

        for (int i=0; i<answer.size(); i++)

        {

            cout << answer[i] << " ";

        }

        cout << endl;

    }

}