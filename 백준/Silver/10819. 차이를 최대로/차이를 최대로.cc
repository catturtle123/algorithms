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


vector<int> t; 

vector<int> o;

int largest;

int absss;

void pick(int n, int m) {
    if (picked.size() == m) { 
        absss = 0;
        for(int i = 0; i < n; i++){
            o[i] = t[picked[i] - 1];
        }
        for(int i = 0; i < n-1; i++){
            absss += abs(o[i] - o[i + 1]);
        }
        largest > absss ? largest = largest : largest = absss;
        return;
    }

    REP (next, 1, n) {
        if (visitied[next]) continue; 
        visitied[next] = true; 
        picked.pb(next);
        pick(n, m); 
        visitied[next] = false; 
        picked.pop_back(); 
    }

}


int main() {
    FAST_IO;
    int n;
    cin >> n;
    t.resize(n);
    o.resize(n);
    rep(i, 0, n) cin >> t[i];
    pick (n, n);
    cout << largest << endl;
    return 0;
}