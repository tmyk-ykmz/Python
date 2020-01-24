package chap02;

import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

public class List_slice {
    public static void main(String[] args) {
        // リスト使用
        List<Integer> n1 = Arrays.asList(1, 3, 5);
        List<Integer> n2 = Arrays.asList(2, 4, 6);

        List<Integer> n3 = new ArrayList<Integer>();

        n3.addAll(n1);
        n3.addAll(n2);

        System.out.println("一覧を表示します");
        System.out.println(n3);

        System.out.println("1番目から2番目までの内容を表示します");
        System.out.println(n3.subList(0, 3));
    }
}
