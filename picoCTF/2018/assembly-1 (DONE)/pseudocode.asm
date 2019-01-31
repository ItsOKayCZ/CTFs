asm1:
	if (param1 > 0x98) {
		goto part_a
	}
	if (param1 != 0x98) {
		goto part_b
	}
	eax = *param1
	eax += 3
	goto part_d

part_a:
	if (param1 != 0x16) {
		goto part_c
	}
	eax = *param1
	eax -= 3
	goto part_d

part_b:
	eax = *param1
	eax -= 3
	goto part_d

	// unreachable
	if (param1 != 0xbc) {
		goto part_c
	}
	eax = *param1
	eax -= 3
	goto part_d

part_c:
	eax = *param1
	eax += 3

part_d:
	return value;