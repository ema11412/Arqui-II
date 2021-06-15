module deco_PC(input logic [1:0] BranchSel,
					input logic eq, blt,
					input logic [1:0] JMPSel,
					output logic [1:0] NextInstrSel);
					
					always_comb 
					begin
						if(BranchSel == 2'b00)
							if(JMPSel == 2'b01)
								NextInstrSel <= 2'b01;
							else if (JMPSel == 2'b10)
								NextInstrSel <= 2'b10;
							else
								NextInstrSel <= 2'b00;
						else if ((BranchSel == 2'b01 && eq) || (BranchSel == 'b10 && blt))
							NextInstrSel <= 2'b11;
						else 
							NextInstrSel <= 2'b00;
					end

endmodule
