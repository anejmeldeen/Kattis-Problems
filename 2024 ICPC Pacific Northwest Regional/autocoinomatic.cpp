#include <iostream>
#include <vector>
#include <set>

using namespace std;
int MAXI = 1e5;

int main() {
    int n, m; cin >> n >> m;
    set<int> seen;
    for (int i = 0; i < n; i++) {
        int coin; cin >> coin;
        seen.emplace(coin);
    }

    vector<char> types(m);
    vector<int> values(m);
    for (int i = 0; i < m; i++) {
        cin >> types[i];
        cin >> values[i];

        if (types[i] == 'X') {
            seen.erase(values[i]);
        }
    }

    vector<int> dp(MAXI + 1, MAXI + 1);
    dp[0] = 0;

    for (int coin : seen) {
        for (int i = 0; i <= MAXI; i++) {
            if (i + coin <= MAXI) {
                dp[i + coin] = min(dp[i + coin], dp[i] + 1);
            }
        }
    }

    vector<int> sol;
    for (int j = m - 1; j >= 0; j--) {
        if (types[j] == 'X') {
            int coin = values[j];
            for (int i = 0; i <= MAXI; i++) {
                if (i + coin <= MAXI) {
                    dp[i + coin] = min(dp[i + coin], dp[i] + 1);
                }
            }
        } else {
            if (dp[values[j]] <= MAXI) {
                sol.push_back(dp[values[j]]);
            } else {
                sol.push_back(-1);
            }
        }
    }

    for (int t = sol.size() - 1; t >= 0; t--) {
        cout << sol[t] << '\n';
    }

    return 0;
}