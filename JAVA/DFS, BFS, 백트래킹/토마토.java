import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
   static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};

    public static int getMaxDay(int[][] box) {
        int maxDay = 0;
        for (int[] b : box) {
            for (int tomato : b) {
                maxDay = Math.max(maxDay, tomato);
            }
        }
        return maxDay - 1;
    }

    public static boolean isAllRiped(int[][] box) {
        for (int[] b : box) {
            for (int tomato : b) {
                if (tomato == 0) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int M = scanner.nextInt();
        int N = scanner.nextInt();
        int[][] box = new int[N][M];
        Queue<int[]> tomatoQueue = new ArrayDeque<>();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                box[i][j] = scanner.nextInt();
                if (box[i][j] == 1) {
                    tomatoQueue.offer(new int[]{i, j});
                }
            }
        }

        while (!tomatoQueue.isEmpty()) {
            int[] tomato = tomatoQueue.poll();
            int x = tomato[0];
            int y = tomato[1];
            int day = box[x][y];
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (0 <= nx && nx < N && 0 <= ny && ny < M && box[nx][ny] == 0) {
                    box[nx][ny] = day + 1;
                    tomatoQueue.offer(new int[]{nx, ny});
                }
            }
        }

        if (!isAllRiped(box)) {
            System.out.println(-1);
        } else {
            System.out.println(getMaxDay(box));
        }
    }
}