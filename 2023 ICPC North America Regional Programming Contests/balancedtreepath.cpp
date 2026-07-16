#include <iostream>
#include <vector>
#include <map>

using namespace std;

int dfs(int node, string& chars, map<int, vector<int>>& graph, vector<int>& stack, int prev) {
    char c = chars[node - 1];
    int curr_stack_len = stack.size();
    map<char, char> rev;
    rev[')'] = '(';
    rev['}'] = '{';
    rev[']'] = '[';

    if (stack.size() > 0 && rev.count(c) && rev[c] == stack[stack.size() - 1]) {
        stack.pop_back();
    } else if (rev.count(c)) {
        return 0;
    } else {
        stack.push_back(c);
    }

    int result = (stack.size() == 0);

    for (int conn : graph[node]) {
        if (conn == prev) continue;
        result += dfs(conn, chars, graph, stack, node);
    }

    if (stack.size() > curr_stack_len) stack.pop_back();
    else if (stack.size() < curr_stack_len) stack.push_back(rev[c]);

    return result;
}

int main() {
    int n; cin >> n;
    string chars; cin >> chars;
    map<int, vector<int>> graph;

    for (int i = 0; i < n - 1; i++) {
        int x, y; cin >> x >> y;
        graph[x].push_back(y);
        graph[y].push_back(x);
    }

    int solution = 0;
    vector<int> stack;
    for (int i = 1; i <= n; i++) {
        solution += dfs(i, chars, graph, stack, -1);
    }
    cout << solution << "\n";

    return 0;
}