module instruction_mem(input logic [31:0] a,
							  output logic [31:0] rd);
							  
							  logic [31:0] RAM [63:0];
							  initial
							   $readmemh("D:\\Tony\\Desktop\\c\\2021s1\\Arqui2\\Proyecto2\\compalfa-asip\\testOut.txt", RAM);
							  assign rd = RAM[a[31:2]];
endmodule


