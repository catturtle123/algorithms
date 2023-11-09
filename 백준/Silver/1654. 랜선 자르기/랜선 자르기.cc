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

vector<int> v;
int n, m;

int check(int val) {
    ll ret = 0;
    rep(i, 0, n) ret += v[i] / val;    
    debugf("%d %d %d\n", ret, m, ret>=m);
    return ret >= m; 
}

int main(void) {
    FAST_IO; 

    ll lo = 1, hi = INT_MAX + 1LL, mid;
    cin >> n >> m;
    v.resize(n);
    rep(i, 0, n) cin >> v[i];

    while (lo + 1 < hi) {
        mid = lo + hi >> 1;
        debugf("%d %d %d\n",lo,hi,mid);
        if (check(mid)) {
            lo = mid;
        } else {
            hi = mid;
        }
    }

    cout << lo << endl;
    // 1 2 ... 10djr
    // t t t ... t f f f f
    return 0;
}