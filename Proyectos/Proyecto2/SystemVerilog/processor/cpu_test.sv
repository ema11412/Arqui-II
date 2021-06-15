`timescale 1 ps/ 1 ps
module cpu_test();

logic clk, reset, image_select;
logic [7:0] d1;
logic [23:0] c1, c2;
logic [31:0] gpu_address;
logic[7:0] vram_out;
integer f, i;
cpu_top DUT(clk, reset, image_select, gpu_address, c1, c2, d1, vram_out);

	initial begin
		
		clk = 1;
		reset = 0;
	
		gpu_address = 0;
		
		#1000 reset = 1;
		#1000 reset = 0;

		c1 = 24'haa00ee;
		c2 = 24'hff33ff;

		d1 = 8'd25;
		// Write original image
		image_select = 0;
		
		//synthesis translate_off
		f = $fopen("C:/Users/roger/Downloads/ASIP-vectorial-para-composicion-alfa/SystemVerilog/outputs/in.txt");
		//synthesis translate_on
		for (i = 0; i < 160000; i = i + 1)
			begin
				gpu_address <= i;
				@(posedge clk)
					$fdisplay(f,"%b", vram_out);
			end
	
	
		#150ns image_select = 1;
		
		//synthesis translate_off
		f = $fopen("C:/Users/roger/Downloads/ASIP-vectorial-para-composicion-alfa/SystemVerilog/outputs/out.txt");
		//synthesis translate_on
		for (i = 0; i < 90000; i = i + 1)
			begin
				gpu_address <= i;
				@(posedge clk)
					$fdisplay(f,"%b", vram_out);
			end
			
	end
	
	always
		#1000 clk <= !clk;

endmodule 