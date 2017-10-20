package itlabsapp;

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

        OutputStream dummyOutputStream = new OutputStream() {
            @Override
            public void write(int i) throws IOException {
                System.out.println("Manual move " + i);
                assertEquals(i,MopedStream.MOV);
            }
        };

        MopedStream testableMopedStream = new MopedStream(dummyOutputStream);

        testableMopedStream.move(testableMopedStream.MOV);

    }

    @Test
    public void turn() throws Exception {

        OutputStream dummyOutputStream = new OutputStream() {
            @Override
            public void write(int i) throws IOException {
                System.out.println("Manual turn " + i);
                assertEquals(i,MopedStream.TRN);
            }
        };

        MopedStream testableMopedStream = new MopedStream(dummyOutputStream);

        testableMopedStream.turn(testableMopedStream.TRN);


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

        testableMopedStream.turn(testableMopedStream.ACC);

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