import java.util.ArrayList;
import  java.util.Collections;
import java.util.Scanner;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Heap {
    public ArrayList<Integer> heapArray = null;

    public Heap() {
        this.heapArray = new ArrayList<Integer>();
        this.heapArray.add(null);
    }

    public boolean move_up(Integer inserted_idx) {
        if (inserted_idx <= 1) {
            return false;
        }
        Integer parent_idx = inserted_idx / 2;
        if (this.heapArray.get(inserted_idx) > this.heapArray.get(parent_idx)) {
            return true;
        } else {
            return false;
        }
    }

    public boolean insert(Integer data) {
        Integer inserted_idx, parent_idx;
        if (this.heapArray == null) {
            this.heapArray = new ArrayList<Integer>();
            this.heapArray.add(null);
            this.heapArray.add(data);
            return true;
        }

        this.heapArray.add(data);
        inserted_idx = this.heapArray.size() - 1;

        while (this.move_up(inserted_idx)) {
            parent_idx = inserted_idx / 2;
            Collections.swap(heapArray, inserted_idx, parent_idx);
            inserted_idx = parent_idx;
        }
        return true;
    }

    public boolean move_down(Integer popped_idx) {
        Integer left_child_popped_idx, right_child_popped_idx;

        left_child_popped_idx = popped_idx * 2;
        right_child_popped_idx = popped_idx * 2 + 1;

        if (left_child_popped_idx >= this.heapArray.size()) {
            return false;
        } else if (right_child_popped_idx >= this.heapArray.size()) {
            if (this.heapArray.get(popped_idx) < this.heapArray.get(left_child_popped_idx)) {
                return true;
            } else {
                return false;
            }
        } else {
            if (this.heapArray.get(left_child_popped_idx) > this.heapArray.get(right_child_popped_idx)) {
                if (this.heapArray.get(popped_idx) < this.heapArray.get(left_child_popped_idx)) {
                    return true;
                } else {
                    return false;
                }
            } else {
                if (this.heapArray.get(popped_idx) < this.heapArray.get(right_child_popped_idx)) {
                    return true;
                } else {
                    return false;
                }
            }
        }
    }

    public Integer pop() {
        Integer returned_data, popped_idx, left_child_popped_idx, right_child_popped_idx;

        if (this.heapArray.size() <= 1) {
            return null;
        }

        returned_data = this.heapArray.get(1);
        this.heapArray.set(1, this.heapArray.get(this.heapArray.size() - 1));
        this.heapArray.remove(this.heapArray.size() - 1);
        popped_idx = 1;

        while (this.move_down(popped_idx)) {
            left_child_popped_idx = popped_idx * 2;
            right_child_popped_idx = popped_idx * 2 + 1;

            if (right_child_popped_idx >= this.heapArray.size()) {
                if (this.heapArray.get(popped_idx) < this.heapArray.get(left_child_popped_idx)) {
                    Collections.swap(this.heapArray, popped_idx, left_child_popped_idx);
                    popped_idx = left_child_popped_idx;
                }
            } else {
                if (this.heapArray.get(left_child_popped_idx) > this.heapArray.get(right_child_popped_idx)) {
                    if (this.heapArray.get(popped_idx) < this.heapArray.get(left_child_popped_idx)) {
                        Collections.swap(this.heapArray, popped_idx, left_child_popped_idx);
                        popped_idx = left_child_popped_idx;
                    }
                } else {
                    if (this.heapArray.get(popped_idx) < this.heapArray.get(right_child_popped_idx)) {
                        Collections.swap(this.heapArray, popped_idx, right_child_popped_idx);
                        popped_idx = right_child_popped_idx;
                    }
                }
            }
        }
        return returned_data;
    }


}

public class Main {
	public static void theDayNext(ArrayList<Integer> before) {
		for(int i = 1; i<before.size(); i++) {
			int temp = before.get(i);
			before.set(i, temp+1);
		}
	}
	
	public static void main(String[] args) throws Exception  {
		Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		long[] result = new long[T];
		
		for(int t =0; t<T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());	
			int D = Integer.parseInt(st.nextToken());
			
			Heap yard = new Heap(); 
			for(int r = 0; r<N; r++) {
				st = new StringTokenizer(br.readLine());
				for(int c=0; c<M; c++) {
					yard.insert(Integer.parseInt(st.nextToken())+1);
				}
			}

			long total_grass = 0;
			
			st = new StringTokenizer(br.readLine());
			for(int d = 0; d<D; d++) {
				long grass = 0;
				int oil = Integer.parseInt(st.nextToken());
				for(int o=0; o<oil; o++) {
					int temp = yard.pop();
					grass += temp-1;
					yard.insert(1);
				}
				total_grass += (d+1)*grass;
				theDayNext(yard.heapArray);
			}
		
			result[t] = total_grass;
		}
		sc.close();
		for(int t =0; t<T; t++) {
			System.out.println("#"+(t+1)+" "+result[t]);
		}
	}
}


