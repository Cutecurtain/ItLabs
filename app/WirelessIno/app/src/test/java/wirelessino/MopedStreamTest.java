package wirelessino;

import org.junit.Test;

import java.io.IOException;
import java.io.OutputStream;

import static org.junit.Assert.*;

/**
 * Created by Eli on 2017-10-19.
 */
public class MopedStreamTest {


    private long a;

    @Test
    public void move() throws Exception {
        OutputStream dummyOutputStream = getDummyOutPutStream();
        MopedStream testableMopedStream = new MopedStream(dummyOutputStream);

        System.out.println("Manual move");
        testableMopedStream.move(testableMopedStream.MOV);
        assertEquals(a,1);

    }

    @Test
    public void turn() throws Exception {
        OutputStream dummyOutputStream = getDummyOutPutStream();
        MopedStream testableMopedStream = new MopedStream(dummyOutputStream);

        System.out.println("Manual turn");
        testableMopedStream.turn(testableMopedStream.TRN);
        assertEquals(a,2);

    }

    @Test
    public void acc() throws Exception {
        OutputStream dummyOutputStream = getDummyOutPutStream();
        MopedStream testableMopedStream = new MopedStream(dummyOutputStream);

        assertFalse(testableMopedStream.getAccStatus());
        testableMopedStream.acc(true);
        assertTrue(testableMopedStream.getAccStatus());
        testableMopedStream.acc(false);
        assertFalse(testableMopedStream.getAccStatus());

    }

    @Test
    public void write() throws Exception {

    }

    @Test
    public void close() throws Exception {

    }


    private OutputStream getDummyOutPutStream(){

        OutputStream dummyOutPut = new OutputStream() {
            @Override
            public void write(int i) throws IOException {
                System.out.println(i);
                a = i;
            }
        };

        return dummyOutPut;
    }


}