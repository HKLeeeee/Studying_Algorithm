import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    static int N, M, V;
    static boolean[][] graph;
    static boolean[] visit;
    static String result = "";

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        V = sc.nextInt();
        graph = new boolean[N + 1][N + 1];
        visit = new boolean[N + 1];

        for (int i = 0; i < M; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph[a][b] = true;
            graph[b][a] = true;
        }

        dfs(V);
        result += "\n";
        bfs(V);

        System.out.println(result);
    }

    public static void dfs(int start) {
        visit[start] = true;
        result += start + " ";

        for (int i = 1; i < N + 1; i++) {
            if (graph[start][i] && !visit[i]) {
                dfs(i);
            }
        }
    }

    public static void bfs(int start) {
        boolean[] visit = new boolean[N + 1];
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(start);
        visit[start] = true;

        while (!queue.isEmpty()) {
            start = queue.poll();
            result += start + " ";

            for (int i = 1; i < N + 1; i++) {
                if (graph[start][i] && !visit[i]) {
                    queue.add(i);
                    visit[i] = true;
                }
            }
        }
    }
}