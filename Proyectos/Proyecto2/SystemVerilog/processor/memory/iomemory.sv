module iomemory(input logic clk, write_enable, 
					input logic[31:0] data_address, address_intr, data_input, gpu_address,
					input logic[31:0] vector_input,
					output logic[7:0] encrypted_gpu, decrypted_gpu,
					output logic[31:0] data_output, intr_output,
					output logic[31:0] vector_output);

logic decrypted_we, ram_we;
logic[31:0] ram_read, ram_data, ram_address, encrypted_address, decrypted_address;

address_decoder AddrDecoder(write_enable, data_address, ram_read, data_input,
ram_we, decrypted_we, ram_address, encrypted_address, decrypted_address, ram_data, data_output);

logic[31:0] address_intr_2;

assign address_intr_2 = address_intr / 4;

isa RAM(ram_address, address_intr_2, clk, ram_data, 'd0, ram_we, 1'b0, ram_read, intr_output);

album base_image(encrypted_address, gpu_address, clk, vector_output, encrypted_gpu);

tram process_image(vector_input, gpu_address, decrypted_address, clk, decrypted_we, decrypted_gpu);

endmodule 