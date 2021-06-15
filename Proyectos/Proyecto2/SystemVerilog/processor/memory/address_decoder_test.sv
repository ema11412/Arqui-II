module address_decoder_test();

logic write_enable, ram_we, decrypted_we;
logic[31:0] address, ram_read, data_input;
logic[31:0] ram_address, encrypted_address, decrypted_address, ram_data, data_output;
												
											
address_decoder DUT(write_enable, address, ram_read, data_input,
ram_we, decrypted_we, ram_address, encrypted_address, decrypted_address, ram_data, data_output);


initial begin
	write_enable = 0; address = 32'h4; ram_read = 32'h999; data_input = 32'hF; 
	
	#10 address = 32'h404;
	#10 write_enable = 1;
	#10 address = 32'h40C;
	#10 write_enable = 0;
	#10 address = 32'h400;
	#10 write_enable = 1;
	#10 address = 32'h30000;
	#10 write_enable = 0;
	#10 address = 32'h4100;
	#10 write_enable = 1;
	#10 write_enable = 0;
	
end
endmodule
										