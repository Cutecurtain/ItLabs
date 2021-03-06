package itlabsapp;
import java.io.IOException;
import java.io.OutputStream;

public class MopedStream extends OutputStream {
	private final OutputStream out;
	public static final byte
		NOP = (byte)0x00,
		MOV = (byte)0x01,
		TRN = (byte)0x02,
		ACC = (byte)0x03,
		BRK = (byte)0xFF;
	private boolean accEnabled = false;

	public MopedStream(OutputStream out) {
		this.out = out;
	}
	public void move(byte b) throws IOException {
		if(!accEnabled) {
			write(MOV);
			write(b);
		}
	}
	public void turn(byte b) throws IOException {
			write(TRN);
			write(b);

	}
	public void acc(boolean enable) throws IOException {
		accEnabled = enable;
		write(ACC);
		write(enable?1:0);
	}

	public boolean getAccStatus(){
		return accEnabled;
	}

	@Override
	public void write(int b) throws IOException {
		out.write(b);
	}
	@Override
	public void close() throws IOException {
		write(BRK);
		out.close();
	}
}
