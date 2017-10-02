package se.sics.sse.fresta.wirelessino;
import java.io.OutputStream;

public class MopedStream extends OutputStream {
	private final OutputStream out;
	public static final byte
		NOP = 0x00,
		MOV = 0x01,
		TRN = 0x02,
		ACC = 0x03,
		BRK = 0xFF;

	public MopedStream(OutputStream out) {
		this.out = out;
	}
	public void move(byte b) {
		write(MOV);
		write(b);
	}
	public void turn(byte b) {
		write(TRN);
		write(b);
	}
	public void acc(boolean enable) {
		write(ACC);
		write(b?1:0);
	}

	@Override
	public void write(int b) {
		out.write(b);
	}
	@Override
	public void close() {
		write(BRK);
		out.close();
	}
}
