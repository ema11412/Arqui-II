module mux_Ifetch (input logic [1:0] NextInstr,
						input logic [31:0] PCplus4,Address, Rs, Branch,
						output logic [31:0]nextPC); // NextInstr viene PC_deco.
						always @(*) begin
							case(NextInstr)
								2'b00 : nextPC <= PCplus4;
								2'b01 : nextPC <= Address;
								2'b10 : nextPC <= Rs;
								2'b11 : nextPC <= Branch;
							endcase
						
						end

endmodule