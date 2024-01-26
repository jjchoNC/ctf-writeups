import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.Map;
import java.util.Scanner;

public class Main {
    private static int a;
    private static long[] b = new long[13];

    public Main() {
    }

    static String a(String var0) {
        byte[] var1 = var0.getBytes(StandardCharsets.UTF_8);
        int var2 = (int) b[0] ^ 2125394058;

        while (var2 <= var0.length()) {
            int var3 = (int) b[1] ^ 316324253;

            while (var3 < var1.length) {
                var1[var3] = (byte) (var1[var3] + (var2 - ((int) b[2] ^ 322717984)) * var3 + ((int) b[3] ^ 1817181337));
                ++var3;
                a = (int) b[4] ^ 1916880556;
                if ((a * a + a + ((int) b[5] ^ 1376134906)) % ((int) b[6] ^ 1536615318) == 0) {
                }
            }
            ++var2;
        }

        return new String(Base64.getEncoder().encode(var1), StandardCharsets.UTF_16);
    }

    public static void main(String[] var0) {
        System.out.println(b(
                "\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a"));
        System.out.println(b(
                "\ucc20\ucc12\ucc1b\ucc14\ucc18\ucc1a\ucc12\ucc57\ucc03\ucc18\ucc57\ucc23\ucc18\ucc03\ucc16\ucc1b\ucc1b\ucc0e\ucc24\ucc12\ucc14\ucc02\ucc05\ucc12\ucc35\ucc16\ucc19\ucc1c\ued55"));
        System.out.println(b(
                "\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a\ucc4a"));
        System.out.println();
        System.exit(a());
    }

    private static int a() {
        Scanner var0 = new Scanner(System.in);
        Map var1 = Map.of(b("\ucc02\ucc04\ucc12\ucc05"), new a(b("\ua645\ua315\ufb40\ubc5c\u9c00\uf14a"), 10.0F),
                b("\ucc16\ucc13\ucc1a\ucc1e\ucc19"),
                new a(b("\ub812\ue311\u8610\uf416\u9c47\u9a22\u9f21\u8b34\uaf3e\ufe3b\ua04f\ua905\ub903\ua50d\uba05\ua23d"),
                        100000.0F));

        while (true) {
            System.out.println(b(
                    "\ucc27\ucc1b\ucc12\ucc16\ucc04\ucc12\ucc57\ucc12\ucc19\ucc03\ucc12\ucc05\ucc57\ucc0e\ucc18\ucc02\ucc05\ucc57\ucc02\ucc04\ucc12\ucc05\ucc19\ucc16\ucc1a\ucc12\ucc4d"));
            String var2 = var0.nextLine();
            if (var1.containsKey(var2)
                    && ((int) b[5] ^ 1376134906) * (a + ((int) b[8] ^ 935365214)) * (a + ((int) b[8] ^ 935365214))
                            - ((int) b[0] ^ 2125394058) - a != 0) {
                while (true) {
                    System.out.println(b(
                            "\ucc27\ucc1b\ucc12\ucc16\ucc04\ucc12\ucc57\ucc12\ucc19\ucc03\ucc12\ucc05\ucc57\ucc0e\ucc18\ucc02\ucc05\ucc57\ucc07\ucc16\ucc04\ucc04\ucc00\ucc18\ucc05\ucc13\ucc4d"));
                    String var3 = var0.nextLine();
                    if (((a) var1.get(var2)).a(var3)) {
                        if ((a + ((int) b[0] ^ 2125394058)) % ((int) b[9] ^ 2029694983) == 0) {
                        }

                        System.out.println("Welcome back " + var2 + "! your balance is " + ((a) var1.get(var2)).a());
                        return (int) b[1] ^ 316324253;
                    }

                    while (true) {
                        System.out.println(b(
                                "\ucc3e\ucc19\ucc14\ucc18\ucc05\ucc05\ucc12\ucc14\ucc03\ucc57\ucc07\ucc16\ucc04\ucc04\ucc00\ucc18\ucc05\ucc13\ucc56"));
                        if ((a + ((int) b[0] ^ 2125394058)) % ((int) b[9] ^ 2029694983) == 0) {
                            continue;
                        }
                    }
                }
            }

            while (true) {
                System.out.println(
                        b("\ucc22\ucc04\ucc12\ucc05\ucc57\ucc19\ucc18\ucc03\ucc57\ucc11\ucc18\ucc02\ucc19\ucc13"));
                if ((a + ((int) b[0] ^ 2125394058)) % ((int) b[9] ^ 2029694983) == 0) {
                    continue;
                }
            }
        }
    }

    public static String b(String var0) {
        StringBuilder var1 = new StringBuilder();
        int var2 = (int) b[1] ^ 316324253;

        while (var2 < var0.length()) {
            char var3 = var0.charAt(var2);
            var1.append((char) (var3 ^ (int) b[10] ^ 538455364));
            ++var2;
        }

        return var1.toString();
    }

    static {
        b[0] = 2125394059L;
        b[1] = 316324253L;
        b[2] = 322717996L;
        b[3] = 1817181343L;
        b[4] = 1916880576L;
        b[5] = 1376134909L;
        b[6] = 1536615367L;
        b[7] = 969122838L;
        b[8] = 935365158L;
        b[9] = 2029694981L;
        b[10] = 538501427L;
        b[11] = 1099949760L;
        b[12] = 977807481L;
        a = (int) b[12] ^ 1155979507;
    }
}
