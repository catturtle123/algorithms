#include <bits/stdc++.h>
#define endl "\n"
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define rrep(i, a, b) for(auto i = a; i > b; --i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
#define RREP(i, a, b) for(auto i = a; i >= b; --i)
#define pii pair<int, int>
#define tii tuple<int, int, int>
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define INF numeric_limits<int>::max()
#define PIV (1 << 20)
using namespace std;

#ifdef ONLINE_JUDGE
constexpr bool ndebug = true;
#else
constexpr bool ndebug = false;
#endif
#define FAST_IO \
    if constexpr (ndebug) { cin.tie(nullptr); ios::sync_with_stdio(false); }
#define debug(x) \
    if constexpr (!ndebug) cout << "[DEBUG] " << #x << " == " << x << '\n';
#define debugf(...) \
    if constexpr (!ndebug) { cout << "[DEBUG] "; printf(__VA_ARGS__); }
#define debugc(c) \
    if constexpr (!ndebug) { cout << "[DEBUG] "<< #c << ": "; for (const auto& elem : c) cout << elem << ", "; cout << '\n'; }

typedef long long ll;
typedef unsigned long long ull;
 
vector<int> picked; 


bool visitied[10]; 


vector<string> t; 
vector<int> o;
vector<int> c;

ll smallest = LONG_LONG_MAX;
ll largest = LONG_LONG_MIN;
ll num;
int k;

void pick(int n, int m) {
     if (picked.size() == m) {
            rep (i, 0, m) o[i] = picked[i];
            k = 0;
            num = 0;
            for(int i = 0; i < m - 1 ; i++) {
                if (t[i] == ">") {
                    o[i] > o[i + 1] ? c[i] = o[i], c[i + 1] = o[i + 1] :  k = -1; 
                } else {
                    o[i] < o[i + 1] ? c[i] = o[i], c[i + 1] = o[i + 1] :  k = -1;
                }
            }


            if(k != -1){
                rep(i, 0, m) num += (o[i] * pow(10, m - i - 1));

                if(largest < num) {
                    largest = num;
                }
                if(smallest > num) {
                    smallest = num;
                }
            }
            return;
        }
        
    for (int next = 0 ; next < n; next++) {
        if (visitied[next]) continue; 
        visitied[next] = true; 
        picked.pb(next);
        pick(n, m); 
        visitied[next] = false; 
        picked.pop_back(); 
    }

}

int sizeofint(ll data)
{
    int pos = 1, i;


    if (data < 0) data *= (-1);

    for (i = 0; ; i++, pos++)
    {
        if ((data /= 10) <= 0)
            break;
    }
    return(pos);
}

int main() {
    FAST_IO;
    int n;
    cin >> n;
    t.resize(n);
    o.resize(n + 1);
    c.resize(n + 1);
    rep(i, 0, n) cin >> t[i];
    pick (10, n + 1);

    int p = sizeofint(largest);
    rep(i, 0, n + 1 - p) cout << 0; 
    cout << largest << endl;

    p = sizeofint(smallest);
    rep(i, 0, n + 1 - p) cout << 0;
    cout << smallest << endl;
    return 0;
}