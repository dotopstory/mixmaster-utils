function NPC_QUEST_355(cnum, reqNumber)


	req = reqNumber
	Lv = GetHeroLv(cnum)


	if req == 1 then
		     		return 5,0,"����~�ȳ��ϽŰ�!@���� ���� ���͵��� ������@��~������! �ٸ�ũ ������ ����!@�ٷ�! �ٸ�ũ��� �ϳ�!@@�� ������ �� �̻� �ʿ������?!@[���ζ� 30�ֳ� ���]����@�� ������ ������ �����ϰڳ�!@�ڳ׿��� �´� ���� ��󺸰�!!",2,"[Lv.1 ~ Lv.50] [�ٸ�ũ ����]",3,"[Lv.51 ~ Lv.100] [�ٸ�ũ ����] ",4,"[Lv.101 ~ Lv.150] [�ٸ�ũ ����]",5,"[Lv.151 ~ Lv.200] [�ٸ�ũ ����]"


	elseif req == 2 then
    if Lv > 0 and Lv < 51 then --> �˻�
      MoveZone(cnum,183,254)
    else --> �ƴҰ��
      return 1,0,"�ȵǳ�! �ڳ�! ������ �ʹ� ���ݾ�!@�� ��ġ���� �л��� ���ΰ�!@������ �϶��~~"
		end

	elseif req == 3 then

    if Lv > 50 and Lv < 101 then --> �˻�
      MoveZone(cnum,184,254)
    else --> �ƴҰ��
      if Lv < 51 then
        return 1,0,"�ȵ�! �ڳװ� ���ϱ� ������ ���� ����� �� ������ �Ƴ�! ����� ������ 51������ �÷��� �� �� �ֳ�!"
      else
      return 1,0,"�ȵǳ�! �ڳ�! ������ �ʹ� ���ݾ�!@�� ��ġ���� �л��� ���ΰ�!@������ �϶��~~"
      end
    end

	elseif req == 4 then
 		if Lv > 100 and Lv < 151 then --> �˻�
      MoveZone(cnum,185,254)
		else --> �ƴҰ��
      if Lv < 101 then
        return 1,0,"�ȵ�! �ڳװ� ���ϱ� ������ ���� ����� �� ������ �Ƴ�! ����� ������ 101������ �÷��� �� �� �ֳ�!"
      else
      return 1,0,"�ȵǳ�! �ڳ�! ������ �ʹ� ���ݾ�!@�� ��ġ���� �л��� ���ΰ�!@������ �϶��~~"
      end
		end

	elseif req == 5 then
 		if Lv > 150 and Lv < 201 then --> �˻�
      MoveZone(cnum,186,254)
		else --> �ƴҰ��
      if Lv < 151 then
        return 1,0,"�ȵ�! �ڳװ� ���ϱ� ������ ���� ����� �� ������ �Ƴ�! ����� ������ 151������ �÷��� �� �� �ֳ�!"
      end
		end
	end
end