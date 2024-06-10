
void main_openShop(void)

{
  undefined4 uVar1;
  int *in_GS_OFFSET;
  undefined **ppuVar2;
  undefined4 uVar3;
  undefined4 uVar4;
  undefined4 uVar5;
  undefined4 in_stack_ffffff94;
  undefined4 in_stack_ffffff98;
  undefined4 in_stack_ffffff9c;
  undefined **local_5c;
  undefined4 local_58;
  undefined4 local_54;
  undefined4 local_50;
  undefined4 local_4c;
  undefined4 local_48;
  undefined4 local_44;
  undefined4 local_2c;
  undefined4 local_28;
  undefined **local_24;
  undefined4 local_20;
  undefined **local_1c;
  undefined4 local_18;
  undefined4 local_14;
  undefined *local_10;
  undefined **local_c;
  undefined *local_8;
  undefined **local_4;
  
  while (&stack0x00000000 <= *(undefined **)(*(int *)(*in_GS_OFFSET + -4) + 8)) {
    local_4 = (undefined **)0x80d3520;
    runtime_morestack_noctxt();
  }
  local_8 = &DAT_080e87c0;
  local_4 = &main_statictmp_0;
  ppuVar2 = &local_8;
  uVar3 = 1;
  uVar4 = 1;
  fmt_Println(ppuVar2,1,1);
  main_stockUp();
  local_10 = &DAT_080e87c0;
  local_c = &main_statictmp_1;
  uVar5 = 1;
  local_28 = in_stack_ffffff94;
  local_24 = ppuVar2;
  fmt_Println(&local_10,1,1);
  uVar1 = 0x28;
  local_1c = local_24;
  do {
    local_18 = 0;
    local_14 = 0;
    local_2c = uVar1;
    local_20 = local_28;
    runtime_convT2E32(&DAT_080e8100,&local_2c);
    local_18 = uVar5;
    fmt_Printf(&DAT_080fede2,0x12,&local_18,1,1);
    uVar5 = uVar4;
    main_menu(local_1c,uVar3,uVar4,local_20,in_stack_ffffff98,in_stack_ffffff9c,uVar1);
    uVar1 = local_44;
    in_stack_ffffff9c = local_48;
    uVar4 = local_54;
    local_1c = local_5c;
    in_stack_ffffff98 = local_4c;
    local_28 = local_50;
    uVar3 = local_58;
  } while( true );
}

