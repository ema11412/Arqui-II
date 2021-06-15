//para mide: input logic [1:0] alfa_type

module memory (input logic clk, reset, write_enable, select_alu,
					input logic[31:0] data_address, instr_address, data_input, ALUresult,
					input logic[31:0] vector_input,
					output logic[7:0] encrypted_gpu, decrypted_gpu,
					input logic[127:0] VALUresult,
					input logic [31:0] gpu_address,
					output logic[31:0] data_output, instr_output,
					output logic[31:0] vector_output,
					output logic[127:0] ALUoutput);


	iomemory mem(clk, write_enable, data_address, instr_address, data_input, gpu_address, vector_input, encrypted_gpu, decrypted_gpu, data_output, instr_output, vector_output);

	always_comb
		case(select_alu)
			
			1'b0 : ALUoutput = {96'd0, ALUresult};
			1'b1 : ALUoutput = VALUresult;
			default : ALUoutput = VALUresult;
		
		endcase
endmodule 