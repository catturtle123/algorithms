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

int cache[1000001];


int oneTo(int x) {
    if(1 <= x && x <= 3) {
        return cache[x];
    }

    int& ret = cache[x];

    if (ret != -1) return ret;

    if(x % 6 == 0) {
        return ret = min(oneTo(x / 3), oneTo(x / 2)) + 1; 
    } else if(x % 3 == 0) {
        return ret = min(oneTo(x / 3), oneTo(x - 1)) + 1; 
    } else if(x % 2 == 0) {
        return ret = min(oneTo(x / 2), oneTo(x - 1)) + 1; 
    } else {
        return ret = oneTo(x - 1) + 1;
    }
    return ret;
}

int main(void) {
    FAST_IO; 
    memset(cache, -1, sizeof(cache));
    int n;  
    cache[1] = 0;
    cache[2] = 1;
    cache[3] = 1;
    cin >> n;
    cout << oneTo(n) << endl;
    return 0;
}