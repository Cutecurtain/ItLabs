import sics.plugin.PlugInComponent;

/**
 * Created by AronS on 2017-09-08.
 */

public class AutoRobyn extends PlugInComponent {

    public static void main(String[] args) {
        AutoRobyn plugin = new AutoRobyn(args);
        plugin.run();
    }

    public AutoRobyn(String[] args) {
        super(args);
    }

    public void init() {

    }

    public void run() {
        init();
        System.out.println("Hello World!");
    }
}
