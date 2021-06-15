`timescale 1 ps/ 1 ps
module memory_test();

	logic clk,  reset, write_enable, select_alu;
	logic[31:0] data_address, instr_address, data_input, ALUresult;
	logic[63:0] vector_input;
	logic[7:0] encrypted_gpu, decrypted_gpu;
	logic[255:0] VALUresult;
	logic[31:0] data_output, instr_output, gpu_address;
	logic[127:0] vector_output;
	logic[255:0] ALUoutput;

	memory DUT(clk, reset, write_enable, select_alu, data_address, instr_address, data_input, ALUresult,
				  vector_input,encrypted_gpu, decrypted_gpu, VALUresult, gpu_address, data_output, instr_output, vector_output, ALUoutput);
					
	initial begin
		clk = 0;

		reset = 1;
		write_enable = 0;
		select_alu = 0;
		data_address = 'd0;
		instr_address = 'd0;
		data_input = 'd0;
		ALUresult = 'd0;
		vector_input = 'd0;
		VALUresult = 'd0;
		
		#10 reset = 0;
		#10 reset = 0;
		
		#20 ALUresult = 'd20;
		#20 VALUresult = 'd9238;
		#20 select_alu = 1'b1;
	end
	always
		begin
		#10 clk <= !clk;
		end

endmodule 