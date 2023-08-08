import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Tomato {
    static int N, M;
    static int[][] box;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        M = sc.nextInt();
        N = sc.nextInt();
        box = new int[N][M];
        int day = 0;

        for(int i = 0; i<N; i++){
            for (int j = 0; j < M; j++) {
                box[i][j] = sc.nextInt();
            }
        }
        // 1인 위치 큐에 넣고 주변 찾기?
        // -1인 위치도 기억해두어야하나?

        int x = 0;
        int y = 0;
        int nx, ny;
        while(!isAllRiped()){
            for(int i=0; i<4; i++){
                nx = x + dx[i];
                ny = y + dy[i];

                // 변수 범위 체크

                // 내가 0인데 사방이 -1 이면 -1 출력, 리턴


            }
        }

    }

    public static boolean isAllRiped(){
        for(int i = 0; i<N; i++){
            for (int j = 0; j < M; j++) {
                if(box[i][j] == 0) return false;
            }
        }
        return true;
    }

}
