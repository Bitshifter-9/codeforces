#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

typedef vector<long long> ve;
typedef pair<long long, long long> pa;
typedef vector<pa> vp;
typedef set<long long> se;
typedef map<long, long> ob;

#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()

#define po_b pop_back
#define po_f pop_front
#define p_b push_back
#define p_f push_front

#define yes cout << "YES\n"
#define no cout << "NO\n"
#define ff first
#define ss second
#define sz(x) (int)(x).size()
#define endl '\n'

#define fo(i, a, b) for (int i = a; i < b; i++)
#define rfo(i, a, b) for (int i = a; i >= b; i--)

#define in_ve(v, n) ve v(n); fo(i, 0, n) cin >> v[i]
#define in_ve2(v, n) ve v; fo(i, 0, n) { ll x; cin >> x; v.p_b(x); }
#define in_se(s, n) se s; fo(i, 0, n) { ll x; cin >> x; s.insert(x); }
#define in_ob(m, n) ob m; fo(i, 0, n) { long k, v; cin >> k >> v; m[k] = v; }
#define in_pa(v, n) vp v(n); fo(i, 0, n) cin >> v[i].ff >> v[i].ss
#define in_mat(m, r, c) vector<ve> m(r, ve(c)); fo(i, 0, r) fo(j, 0, c) cin >> m[i][j]
#define in_vs(v, n) vector<string> v(n); fo(i, 0, n) cin >> v[i]
#define in_str(s) string s; getline(cin >> ws, s)

#define out_ve(v) for (auto x : v) cout << x << ' '; cout << endl
#define out_se(s) for (auto x : s) cout << x << ' '; cout << endl
#define out_ob(m) for (auto [k, v] : m) cout << k << " => " << v << endl
#define out_pa(v) for (auto [a, b] : v) cout << a << ' ' << b << endl


const ll MOD = 1e9 + 7;
const ll INF = 1e18;

void fast_io() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}

int main() {
    fast_io();
    ll n,k;
    cin>>n>>k;
    in_ve(lis,n);
    ve arr(n,0);
    ll cou=0;
    ll cou_n=0;
    for (ll i=0;i<n;i++){
        if(lis[i]%k==0){
            cou++;
        }else{
            cou_n++;
        }
        arr[i]=cou;


    }
    out_ve(arr);
    

   
    return 0;
}