package chap02;

import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

public class List_list {
    public static void main(String[] args) {
        // リスト使用
        List<Integer> n1 = Arrays.asList(1, 3, 5);
        List<Integer> n2 = Arrays.asList(2, 4, 6);

        List<Integer> n3 = new ArrayList<Integer>();

        /* n3 = n1 + n2;
         *
         * Javaでは
         * リスト同士の結合に、＋演算子は使えない
         * ↓
         * ↓（Javaの場合）
         */
        n3.addAll(n1);
        n3.addAll(n2);

        System.out.println("一覧を表示します");
        System.out.println(n3);
    }
}
