﻿define e = Character('아이린', color="#c8ffc8")
define s = Character('서은', color="#222")

label left:
    $ gui.direction = 0.25
    $ gui.xdirection = 0.0
    $ gui.rebuild()
    return

label right:
    $ gui.direction = 0.75
    $ gui.xdirection = 1.0
    $ gui.rebuild()
    return

image ch01_bg = "b.png"
label start:

    call ch01_main
    call ch02_main

    return

label ch01_main:
    scene ch01_bg
    "2008년, 봄. XX고등학교."
    s "…야."
    "어디선가 목소리가 들린다."
    s "야."
    "목소리가 꽤 또렷하게 들리지만 고개는 여전히 무겁다. 아직 일어나기 싫다."
    call right
    s "일어나. 점심시간이야."
    "몽롱한 정신으로 고개를 들어 보니 어느 여자아이가 서 있다."
    s "점심시간이라니까? 수업 중에 잠이나 자고. 양아치네. 아무튼 점심 먹으러 안 가?"
    menu:
        "갈게 갈게":
            s "그럼 빨리 일어나. 너 때문에 밥 먹을 시간이 줄고 있잖아."
        "안먹을래":
            s "지금 가야 맛있는 것 많이 먹을 수 있단 말이야. 빨리 나와."
        "의이에에이ㅣ잉??!???!":
            s "갑자기 무슨 헛소리야. 빨리 나오기나 해. 나 배고파."
    #call ar ("ch01_ans")
    #if ch01_ans == "pos":
    #    s "그럼 빨리 일어나. 너 때문에 밥 먹을 시간이 줄고 있잖아." 
    #elif ch01_ans == "neg":
    #    s "지금 가야 맛있는 것 많이 먹을 수 있단 말이야. 빨리 나와."
    #else:
    #   s "갑자기 무슨 헛소리야. 빨리 나오기나 해. 나 배고파."
    "이럴 거면 왜 물어 본건지… 결국 잠이 덜 깬 몸을 일으켜 급식실로 향한다."
    return

label ch02_main
    이 아이의 이름은 서은. 당찬 성격인 아이라서 매번 나를 이런 식으로 질질 끌고 간다. 
가끔 피곤하기는 하지만, 밉지는 않은. 3년째 붙어 다니는 나의 친구다.
[A] 그나저나 날씨, 완전 따뜻해졌지 않아?
[I] 긍정 - “(answer)” 부정 - “(answer)”
[A] 긍정 – “그렇다니까. 벌써 부산 쪽은 벚꽃 다 펴서 이미 진다더라.”
부정 – “이게? 원래 추위 많이 탔었나. 아무튼 약한 척 좀 하지마.”
관계 없는 얘기 – “그 얘기가 왜 여기서 나와. 날씨가 따뜻해지지 않았냐고 물었잖아.”
[A] 꽃구경 간 지가 언젠지를 모르겠다. 올해는 수능도 봐서 더 가기 눈치 보인다니까. 그런데 약간 올해에 더 가고 싶다고 느끼는 것 같아. 일탈 같은 느낌이잖아.
[I] 긍정 – “(answer)” 부정 - “(answer)” 꽃구경 가자고 한다 - “(answer)” 
[A] 긍정 – “앗, 그러면 오늘 나랑 같이 꽃구경 갈래? 나 혼자서 가면 죄책감들 것 같단 말이야.”
부정 – “모범생인 척 좀 하지마. 그런 김에 나랑 오늘 벚꽃 보러 가자. 나 혼자 가면 심심해.”
꽃구경 가자고 한다 – “엥? 너랑? 어... 그래! 좋지. 근데 나 오늘 밖에 시간 안 되는데 괜찮아?”
[I] 꽃구경 거절 – “(answer)” 꽃구경 승낙 - “(answer)” 
[A] 승낙 – “으음, 근데 나 오늘 밖에 시간 안되는데 괜찮아? 오늘 학교 끝나고 바로!” 
거절 – “그렇지? 네가 나랑 꽃구경을 갈 리가 없지. 밥 다 먹었으니까 난 먼저 교실 간다!”
[I] 오늘로 승낙 - “(answer)” 오늘은 거절 - “(answer)”
[A] 승낙 – “그럼 수업 다 끝나고 보자!”
거절 – “벚꽃 다 질 텐데… 그럼 내년에 가지 뭐. 수능도 다 끝나고 대학생일 테니까 시간도 많..지 않으려나. 아무튼! 난 먼저 교실 갈게.”
[N] 꽃구경 가는 것이 그렇게 기쁜 일인가. 방방 뛰면서 올라가는 서은의 모습에 괜시리 웃음이 난다. 나도 슬슬 일어나서 다시 교실로 돌아가도록 하자.
[N2] 이상하다. 평소 같은 모습인데 미묘하게 슬퍼 보였다. 하지만 곧 수업 시간이다. 생각을 그만두고 교실로 돌아가야 한다. 괜찮을거야. 항상 바보만치 밝은 애니까. 그런 애니까.


label ch03_main
    [B] “나랑 얘기 좀 해.”
[N] 누군가가 갑자기 나를 불러 세운다. 옆 반의 B였다. 나랑 친하지도 않은 애가, 갑자기?
[B] “할 얘기가 있어.”
[I] 승낙 – “(answer)” 거절 - “(answer)”
[B] 승낙 – “서은이에 대한 건데..”
거절 – “서은이에 관한 이야기야. 들어줬으면 좋겠어..”
[N] 참, 볼수록 서은이와 정반대되는 성격이다. 무뚝뚝하고, 소심한 말투. 얘기를 들을까?
[I] 승낙 - “(answer)” 거절 - “(answer)”
[B] 승낙 – “서은이에게 얘기하지 않을 거지?”
거절 – “완고하네. 알겠어. 다만, 어떤 소문이 돌아다녀도 듣지마.”
[I] 얘기하지 않겠다 - “(answer)” 들어보고 결정하겠다 - “(answer)”
[B] “그래, 그건 네 선택이니까. 아무튼, 서은이가 너에 대해서 좋지 않은 소문을 퍼트리고 다녀.”
[I] 이유 - “(answer)” (화난, 평이한, 슬픈)
[B] 화난 어조 – “목소리 좀 낮춰줘. 애들이 다 듣겠다. 아무튼,”
평이한 – “그게 말이야.”
슬픈 – “울지는 마.. 뭐라고 했냐면”
+ “네가 이 사람 저 사람 찔러보고 다닌다고도 하고, 사람을 계획적으로 이용한다고 했어. 나도 지나가다 들은 거여서 정확하지는 않은데, 네가 알아야 할 것 같아서.”
[I] 화난 - “(answer)” 슬픈 - “(answer)” 이걸 말해주는 이유가 뭔지 - “(answer)” 서은이가 그럴 리 없다 - “(answer)”
[B] 화난 – “제발, 화내지 말아줘.”
슬픈 – “어.. 충격 받은 건 알겠지만 정신 똑바로 차리길 바라. 아직까지도 소문은 돌고 있어.”
이유 – “그냥, 서은이가 어떤 애인지 알기를 바랐어. 너네 3년 내내 붙어 다녔잖아.” (다시 I의 반응, 감정 상태에 따른 대답 리턴)
그럴 리 없어요 – “믿던 말던 그건 너의 자유기는 해. 하지만 적어도 3학년 내에서는 소문이 쫙 돌았어. 잘 판단하길 바랄게.”
+”더 자세한 이야기가 듣고 싶으면 학교 끝나고 나를 찾아오기를 바라.”
[N] 대답도 듣지 않은 채 B는 자신의 반으로 급하게 들어가버렸다. 나도 일단 교실로 들어가야겠다.


label ch04_b
    [N] 수업에 전혀 집중이 되지 않았다.
[N] 사실일까? 서은이가 정말로 그랬을까? 아냐 그럴 리가 없어.
[N] 사실이라면, 왜 그랬을까? 3년 동안 대체 나는 서은이와 무슨 사이였던 걸까?
[N] 친구? 애초에 친구는 맞았던 것일까?
[N] 아니다. 섣부른 판단은 금물이다. 당사자와 이야기를 나눠봐야 한다.
[N] 하지만 진실이 두렵다. 나는 어떻게 해야 할까..

label ch04_nob
[N] 항상 느끼는 거지만
[N] 수업 시간은 너무.. 졸리다..
[N] 그나저나 B가 하려던 이야기는 뭐였을까?
[N] 시답지 않은 이야기였겠지. 잠이나 자자.

label ch05_main
[A] “…야.”
[N] 서은이다. 표정이 많이 어두워 보인다.
[A] “나한테, 물어볼 것 없어?”
[I] 긍정 – “있어.” (화난/슬픈, 평이) 부정 – “없어.” (화난/슬픈, 평이)
[A] 
긍정 평이 – “그 소문에 관한 것이지?”
부정 평이 – 들었을 것 아냐. 내가 너에 대해서 이상한 소문을 퍼트리고 다닌다는 거.
긍정/부정 화난/슬픈 – 너, 그 말들을 믿는구나? 그래서 화가 난거지?
[I] 긍정 - “(answer)” 부정 - “(answer)”
[A] 긍정 – “내가 정말 그랬을 거라고 생각하는 거야? 그런 바보 같은 소문을 믿는 너도 참 병신이다.
부정 – “또 거짓말. 결국 너도 나를 못 믿잖아. 못 믿으니까 그런 반응인 것 아냐? 3년 동안이나 같이 지내면서 어떻게 나에 대해서 그렇게 한치도 모를 수가 있어?”
긍정 평이 후 부정일 경우 – “뭐가 궁금한데?” -> “그럼 소문에 대한 건 하나도 듣지 못했어?” -> “3학년 내에 소문이 그렇게 퍼졌는데 너만 모른다고? 거짓말하지마.” -> 긍정, 부정
[I] 감정적인 대답(추후에 대화 알고리즘 짤 때 자세하게 적을게요 살려주세요. 예상 답안이 너무 많아요.) - 그 말을 믿는 경우와 믿지 않는 경우로 나뉨
[A] 싸우자싸ㅣ워 – 말을 믿는 경우의 반응(더욱더 감정적)과 믿지 않는 경우의 반응(누그러짐)으로 나뉨
[I] 히힣ㅎ ㅣ싸운다 싸워 – 믿지 않는 경우, 서은이를 누그러뜨리고 믿는다는 것을 확실히 보여줘야 함.
[A] 또 싸우자 히힣히 – 서은이를 확실히 믿는 ‘나’에게 사과하고 마무리된다. 믿지 않는 경우, 서은이와의 벚꽃 약속이 무산되며 결국 자리를 박차고 나가게 된다.

label ch06_main
서은이와 화해한 경우에만 발생하는 이벤트
[N] 나에게는 두 가지 선택만이 남았다.
[N] 서은이와의 약속을 지킬 것인지, 나의 호기심 때문에 B를 만날 것인지.
[선택 이벤트 발생]

label ch07_end
[N] 2018년 봄, 레스토랑 앞..
[N] 오늘은 고등학교 동창회다. 벌써 서른을 앞둔 나이에 고등학교 친구들을 다시 볼 생각하니 조금은 들뜬 마음이다.
[N] 사실, 제일 궁금한 건 서은이였다. 3년을 붙어 다닌, 피곤하지만 밉지 않은 나의 친구.
[N] 벌써부터 북적거리는 레스토랑 안은 친숙하면서도 낯선 사람들로 가득 차있다. 성인이 된다는 것에 막연한 불안함이 있던 열아홉은 하나도 없었다. 그때보다 부쩍 자라버린 어른들만 있을 뿐이었다. 기분이 묘했다.
[N] 많은 친구들과 반갑게 인사를 하며 안부를 묻는 중에도 내 눈은 계속 서은이를 찾고 있었다. 하지만 보이지를 않는다. 이런 자리에 빠질 애가 아닐텐데.. 
[B] “오랜만이네. 잘 지냈어?”
[I] 적당히 긍정적인 반응 - “(answer)” 안부 묻기 - “(answer)” 부정적인 반응 - “(answer)”
[B] 긍정적인 반응 – “그렇구나. 좋아 보이네.”
안부 묻기 – “응 나도 잘 지냈어. 얼마 전에 겨우 취직했거든. 이제 좀 살 맛 나지.”
부정적인 반응 – “오랜만에 본 사인데 너무한 것 아냐?”
[N] B라면 서은이의 행방을 알고 있을지도 모른다. 물어보자.
[I] “서은이 어디 있는지 알아?”
[B] “…농담하는 거지?”
[I] 이유 묻기 - “(answer)” 긍정 - “(answer)” 부정 - “(answer)”
[B] “장난치지마. 나 이런 장난 싫어해.”
[N] B의 표정이 많이 불안해 보인다. 작은 질문으로 아이들의 술렁임이 느껴진다. 대체, 왜? 

label ch08_bad_rev
[B] “정말 기억 안나? 서은이는”
[B] “서은이는 죽었잖아. 10년 전 오늘. 학교에서.”
[N] 정신이 멍해진다. 서은이가 죽었다고?
[B] “교통사고였어. 정말로 기억이 안나? 너 오늘 좀 이상하다.”
[N] 서은이가 죽었다고? 대체 왜?
[N] 멍해진 정신이 좀 더 흐릿해진다. 눈 앞이 아득하다. 몸이 기울어진다.
[B] “…야! 정신차려!!”
[N] 기억이 어긋난 것처럼 아파온다. 억지로 들어낸 것처럼 지운 자국이 선명하다. 
[N] 서은이가 그랬을 리 없다. 서은이가 죽었을 리 없다. 혼란스럽다. 그 때였다.
[???] “당신이 과거에 했을 작은 선택으로 모든 것을 바꿀 수 있다면?”
[N] 칠흑 같은 어둠 속에서 의문의 목소리가 들려온다.
[???] “그 선택으로 소중한 사람을 살릴 수 있다면?”
[N] 서은이를 살릴 수 있을까? 하지만, 이미 10년 전에 죽은 아이를 어떻게?
[???] “잘 생각해봐. 그 날의 너를.”
[N] 수수께끼 같은 말과 함께 다시 나는 끝없는 어둠 속으로 추락했다.
[N] 아래로.. 아래로.. 아래로..
(다시 시작, 프로파일 힌트가 주어진다.)