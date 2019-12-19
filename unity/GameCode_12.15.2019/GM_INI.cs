using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GM_INI : MonoBehaviour
{
    static int Spade_num = 5;
    static int Heart_num = 5;
    static int Diamond_num = 5;
    static int Club_num = 5;
    static int Spade_red_num = 5;
    static int Heart_red_num = 5;
    static int Diamond_red_num = 5;
    static int Club_red_num = 5;

    public Object poker_Spade;
    public Object poker_Heart;
    public Object poker_Diamond;
    public Object poker_Club;
    public Object poker_red_Spade;
    public Object poker_red_Heart;
    public Object poker_red_Diamond;
    public Object poker_red_Club;

    // Start is called before the first frame update
    void Start()
    {
        Spade_num = 5;
        Heart_num = 5;
        Diamond_num = 5;
        Club_num = 5;
        Spade_red_num = 5;
        Heart_red_num = 5;
        Diamond_red_num = 5;
        Club_red_num = 5;
        initMap();
    }

    // Update is called once per frame
    void Update()
    {

    }

    void initMap()
    {
        Vector3 v2_3 = new Vector3();
        Quaternion q = new Quaternion(0, 0, 0, 0);
        for (int i = 39; i >= 0; i--)
        {
            if (Spade_num > 0)
            {
                Spade_num--;
                v2_3 = pos(i);
                Instantiate(poker_Spade, v2_3, q);
            }
            else if (Heart_num > 0)
            {
                Heart_num--;
                v2_3 = pos(i);
                Instantiate(poker_Heart, v2_3, q);
            }
            else if (Diamond_num > 0)
            {
                Diamond_num--;
                v2_3 = pos(i);
                Instantiate(poker_Diamond, v2_3, q);
            }
            else if (Club_num > 0)
            {
                Club_num--;
                v2_3 = pos(i);
                Instantiate(poker_Club, v2_3, q);
            }
            else if (Spade_red_num > 0)
            {
                Spade_red_num--;
                v2_3 = pos(i);
                Instantiate(poker_red_Spade, v2_3, q);
            }
            else if (Heart_red_num > 0)
            {
                Heart_red_num--;
                v2_3 = pos(i);
                Instantiate(poker_red_Heart, v2_3, q);
            }
            else if (Diamond_red_num > 0)
            {
                Diamond_red_num--;
                v2_3 = pos(i);
                Instantiate(poker_red_Diamond, v2_3, q);
            }
            else if (Club_red_num > 0)
            {
                Club_red_num--;
                v2_3 = pos(i);
                Instantiate(poker_red_Club, v2_3, q);
            }
        }
    }

    Vector2 pos(int n)
    {
        float x = -8.0f + (n % 10) * 1.6f;
        float y = -3.7f + (n / 10) * 2.5f;
        return new Vector2(x, y);
    }
}

