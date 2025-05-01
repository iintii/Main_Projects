#include "raylib.h"
#include <vector>
/* Understanding delta time: In current implimentation, velocity and positional variables scales with FPS. To make them independent of FPS we introduce delta time which is inversely proportional to FPS. For example if we want to make vel 10m/s instead of 10m/frame we use delta time as a multiplier for velocity so even if frame rate changes, the program can keep the positional and speed changes constant using delta time. Essentially the object wont slow down or speed up because there is an FPS change.*/

struct AnimData
{
    Rectangle rec;
    Vector2 pos;
    int frame;
    float updateTime;
    float runningTime;
};

// is scarfy on the ground function
bool isOnGround(AnimData data, int windowheight)
{
    return data.pos.y >= windowheight - data.rec.height;
}

// Animation updater function

AnimData updateAnimData(AnimData data, float deltaTime, float spriteNum) // if we make changes to the data.x value, because data is a copy, it wont change the actual scardydata values. We need to set the data type of the function to animdata instead of void and then set scardydata to the funtion.
{
    data.runningTime += deltaTime;
    if (data.runningTime >= data.updateTime)
    {
        data.runningTime = 0.0;

        // update animation
        data.rec.x = data.frame * data.rec.width;
        data.frame++;

        if (data.frame > spriteNum)
        {
            data.frame = 0;
        }
    }
    return data; // return an anim data
}

AnimData scarfyMovement(int amount_moved, AnimData data, int windowwidth, int windowheight)
{
    if (IsKeyDown(KEY_D) && data.pos.x <= (windowwidth - data.rec.width))
    {
        data.pos.x += amount_moved;
    }
    else if (IsKeyDown(KEY_A) && data.pos.x > 0)
    {
        data.pos.x -= amount_moved;
    }
    else if (IsKeyDown(KEY_W) && data.pos.y > 0)
    {
        data.pos.y -= amount_moved;
    }
    else if (IsKeyDown(KEY_S) && data.pos.y < (windowheight - data.rec.height))
    {
        data.pos.y += amount_moved;
    }

    return data;
}

// MENU
void ResetGame(AnimData &scarfyData, std::vector<AnimData> &nebulae, std::vector<AnimData> &nebulaeVert_array,
               float &bgX, float &bgMid, float &bgFore, float &vertSpawnTimer, float &finishLine,
               const int window_width, const int window_height, Texture2D scarfy, Texture2D nebula,
               const int number_of_horizontal_nebula)
{
    // Reset collision and scrolling
    // (Assuming collision is a local variable
    bgX = 0;
    bgMid = 0;
    bgFore = 0;
    vertSpawnTimer = 0;

    // Reset scarfyData
    scarfyData.rec = {0, 0, static_cast<float>(scarfy.width) / 6, static_cast<float>(scarfy.height)};
    scarfyData.pos = {window_width / 2 - scarfyData.rec.width / 2, window_height - scarfyData.rec.height};
    scarfyData.frame = 0;
    scarfyData.runningTime = 0.0f;

    // Clear nebula vectors and repopulate horizontal nebulas
    nebulae.clear();
    for (int i = 0; i < number_of_horizontal_nebula; i++)
    {
        AnimData nebulaData{
            {0.0, 0.0, static_cast<float>(nebula.width) / 8, static_cast<float>(nebula.height) / 8},
            {window_width + (i * 600), window_height - static_cast<float>(nebula.height) / 8},
            0,
            1.0f / 50.0f,
            0.0f};
        nebulae.push_back(nebulaData);
    }
    nebulaeVert_array.clear();

    // Reset finish line based on the horizontal nebulas
    finishLine = nebulae[number_of_horizontal_nebula - 1].pos.x;
}

int main()
{

    // window dimensions
    const int window_width{900};
    const int window_height{600};

    // Initialize window
    InitWindow(window_width, window_height, "Dasher");
    SetTargetFPS(100);

    // gravity
    const int gravity{2000}; //(pix/sec)/sec using delta time

    // BackGround Textures
    Texture2D background = LoadTexture("textures/far-buildings.png");
    float bgX{}; // bacground scroller

    // midground
    Texture2D midground = LoadTexture("textures/back-buildings.png");
    float bgMid{};

    // foreground
    Texture2D foreground = LoadTexture("textures/foreground.png");
    float bgFore{};

    //---------------------------------------------------------------------------------------------

    // Sprite, Compound Data Types (similar to a class)
    Texture2D scarfy = LoadTexture("textures/scarfy.png");

    AnimData scarfyData;
    scarfyData.rec = {0, 0, static_cast<float>(scarfy.width) / 6, static_cast<float>(scarfy.height)};          // Each img from the spritesheet
    scarfyData.pos = {(window_width / 2 - scarfyData.rec.width / 2), (window_height - scarfyData.rec.height)}; // pos of each img
    scarfyData.frame = {};
    scarfyData.updateTime = 1.0 / 12.0;
    scarfyData.runningTime = {};

    //-------------------------------------------------------------------------------------------------
    const int number_of_horizontal_nebula{10};
    const int number_of_vertical_nebula{1};
    // Sprite, Nebula Variables
    Texture2D nebula = LoadTexture("textures/12_nebula_spritesheet.png");

    // Horizontal Nebula

    std::vector<AnimData> nebulae; // vector is an array with changable size. <> holds the type of data.
    for (int i = 0; i < number_of_horizontal_nebula; i++)
    {
        AnimData nebulaData{
            {0.0, 0.0, static_cast<float>(nebula.width) / 8, static_cast<float>(nebula.height) / 8},
            // Vector2 Pos
            {window_width + (i * 600), window_height - nebulaData.rec.height},
            0,            // nebula frame
            {1.0 / 50.0}, // float nebula update time
            0             // float runningtime
        };
        nebulae.push_back(nebulaData); // push nebulas into the vector
    }

    // Vertical Nebula Vector Ini
    std::vector<AnimData> nebulaeVert_array; // vector is an array with changable size. <> holds the type of data.

    // finish line
    float finishLine{nebulae[number_of_horizontal_nebula - 1].pos.x};

    //-------------------------------------------------------------------------------------------------

    int nebVel{600}; // nebula velocity pix/sec

    // rectangle dimensions
    int velocity{0}; // negative y dir ie upwards from the bottom of the window

    // For jumping
    bool isInAir{};
    // jump height
    const int jump_vel{700}; // pix/sec

    // Spawn Timer
    const float vertSpawnDelay{2.0};
    float vertSpawnTimer{};

    // collision
    bool collision{};
    bool win = false;

    //---------------------------------------------------------------------------------------------

    // Each iter is a frame
    while (!WindowShouldClose())
    {

        // Reset game state variables
        collision = false;
        win = false;
        ResetGame(scarfyData, nebulae, nebulaeVert_array, bgX, bgMid, bgFore, vertSpawnTimer,
                  finishLine, window_width, window_height, scarfy, nebula, number_of_horizontal_nebula);
        while (!WindowShouldClose())
        {

            // game over
            if (collision)
            {
                break;
            }

            // deltaTimeMultiplier
            const float dT{GetFrameTime()};

            BeginDrawing();
            ClearBackground(WHITE);

            // background texture----------------------------------------------------------------------
            bgX -= 60 * dT; // scroll speed of background
            if (bgX <= -background.width * 3.55)
            {
                bgX = 0.0; // reset x value as soon as it reaches the background texture * multiplier
            }
            Vector2 bg1Pos{bgX, 0.0};
            DrawTextureEx(background, bg1Pos, 0.0, 3.55, WHITE);
            Vector2 bg2Pos{bgX + background.width * 3.55, 0.0}; // background duplcation
            DrawTextureEx(background, bg2Pos, 0.0, 3.55, WHITE);

            // midground--------------------------------------------------------------------------------

            bgMid -= 80 * dT; // scroll speed of background
            if (bgMid <= -midground.width * 3.55)
            {
                bgMid = 0.0; // reset x value as soon as it reaches the background texture * multiplier
            }
            Vector2 mid1Pos{bgMid, 0.0};
            DrawTextureEx(midground, mid1Pos, 0.0, 3.55, WHITE);
            Vector2 mid2Pos{bgMid + midground.width * 3.55, 0.0}; // background duplcation
            DrawTextureEx(midground, mid2Pos, 0.0, 3.55, WHITE);

            // foreground-------------------------------------------------------------------------------

            bgFore -= 100 * dT; // scroll speed of background
            if (bgFore <= -foreground.width * 3.55)
            {
                bgFore = 0.0; // reset x value as soon as it reaches the background texture * multiplier
            }
            Vector2 fore1Pos{bgFore, 0.0};
            DrawTextureEx(foreground, fore1Pos, 0.0, 3.55, WHITE);
            Vector2 fore2Pos{bgFore + foreground.width * 3.55, 0.0}; // background duplcation
            DrawTextureEx(foreground, fore2Pos, 0.0, 3.55, WHITE);

            // game logic begins

            //-----------------------------------------------------------------------------------------

            // scarfyMovement
            scarfyData = scarfyMovement(5, scarfyData, window_width, window_height);

            // Vertical Nebula
            // Use spawn timer and dT to stagger the pupulation of the vert nebula array so that they are not populated at the same time and thus not pushed to screen at the same time. So taking advantage of the while loop frames and time between each frames ie dT to stagger the population of the vert nebula array. Because the vertnebula obj is defined inside the loop, only a certain amount of data is being sent to the for ranged loop below it per frame.

            vertSpawnTimer += dT;
            if (vertSpawnTimer >= vertSpawnDelay)
            {
                vertSpawnTimer = 0;

                for (int i = 0; i < number_of_vertical_nebula; i++)
                {
                    AnimData VertnebulaData{
                        {0.0, 0.0, static_cast<float>(nebula.width) / 8, static_cast<float>(nebula.height) / 8},
                        // Vector2 Pos, for vertical, use an rng generator for the x positions
                        {scarfyData.pos.x, -VertnebulaData.rec.height},
                        0,            // nebula frame
                        {1.0 / 50.0}, // float nebula update time
                        0             // float runningtime
                    };
                    nebulaeVert_array.push_back(VertnebulaData); // push nebulas into the vector. BEcuse of the forloop ver array is being populated at the same time
                }
            }

            //----------------------------------------------------------------------------------------

            // Ground Check (check after every posY change)
            if (isOnGround(scarfyData, window_height))
            {
                scarfyData.pos.y = window_height - scarfyData.rec.height;
                velocity = 0;
                isInAir = false;
            }
            else
            {
                // add gravity amt per frame
                velocity += gravity * dT;
                isInAir = true;
            }

            // Jumping: Double jump and not
            if (IsKeyPressed(KEY_SPACE) && !isInAir)
            {
                velocity -= jump_vel;
            }

            scarfyData.pos.y += velocity * dT; // NOTE: Falling is simulated because posY is being updated every frame by gravity. posY isnt bound by a conditional

            // Running Time update
            /*  Consistent Animation Speed:
            No matter what the FPS is, the sprite will update its animation only every updateTime seconds. This makes the movement smooth and consistent.

            Frame-Rate Independence:
            If your game runs slower (or faster), the dT adjusts accordingly. For example:
            At 120 FPS, dT might be around 0.0083 seconds. It takes roughly 10 frames (0.0083 * 10 ≈ 0.083 seconds) to reach the update threshold.

            At 60 FPS, dT might be around 0.0167 seconds. It takes roughly 5 frames (0.0167 * 5 ≈ 0.083 seconds) to reach the same threshold.

            so update time is like a trip wire and trigger to trigger the next frame. we use runnign time to determine how soon or late we want to trigger the next frame. If the fps is high that means that the animation frames are wanting to change quickly. Because dT is inverse, dT will slow down the triggering of the next animation frame. If Fps is low we want to speed up the animation frame change, so Dt accumulates quickly and triggers the next frame faster to keep the change in animation frames constant regardless of FPS. runningTime >= updateTime condition is the trip wire.
            Imagine running time getitng "sprinting to" update time slowly or quickly (to change to the next animation frame) depending on dT accumulation */

            scarfyData = updateAnimData(scarfyData, dT, 5); // update scarfy animation

            //-----------------------------------------------------------------------------------------
            // Horizontal nebula
            int crossedCount = 0;
            for (auto &nebData : nebulae)
            {                                 // nebulae is thee name of the vector
                nebData.pos.x -= nebVel * dT; // update pos data for each nebula obj

                // update each nebula animation frame
                nebData = updateAnimData(nebData, dT, 8);

                DrawTextureRec(nebula, nebData.rec, nebData.pos, WHITE); // if number of nebula is set to 4 it will print 4 nebulas per frame due to the forloop.

                // collision check. we wont use nebData.pos because we are modifying the hitboz of each nebula obj and scarfy by refefining each hitbox
                float pad{40}; // adjust nebula hitbox
                Rectangle nebRec{
                    nebData.pos.x + pad,
                    nebData.pos.y + pad,
                    nebData.rec.width - 2 * pad,
                    nebData.rec.height - 2 * pad};

                Rectangle scarfyRec{
                    scarfyData.pos.x,
                    scarfyData.pos.y,
                    scarfyData.rec.width,
                    scarfyData.rec.height};

                if (CheckCollisionRecs(nebRec, scarfyRec))
                {
                    collision = true;
                }

                if (nebData.pos.x + nebData.rec.width < 0)
                {
                    crossedCount++;
                }
            }

            if (crossedCount >= number_of_horizontal_nebula)
            {
                win = true;
                collision = true; // Break out of the game loop.
            }

            // finish line
            finishLine += nebVel * dT;

            // Vertical Nebula
            for (auto &nebData : nebulaeVert_array)
            {                                 // nebulae is thee name of the vector
                nebData.pos.y += nebVel * dT; // update pos data for each nebula obj

                // update each nebula animation frame
                nebData = updateAnimData(nebData, dT, 8);

                DrawTextureRec(nebula, nebData.rec, nebData.pos, WHITE); // if number of nebula is set to 4 it will print 4 nebulas per frame due to the forloop.

                float pad{40}; // adjust nebula hitbox
                Rectangle nebRec{
                    nebData.pos.x + pad,
                    nebData.pos.y + pad,
                    nebData.rec.width - 2 * pad,
                    nebData.rec.height - 2 * pad};

                Rectangle scarfyRec{
                    scarfyData.pos.x,
                    scarfyData.pos.y,
                    scarfyData.rec.width,
                    scarfyData.rec.height};

                if (CheckCollisionRecs(nebRec, scarfyRec))
                {
                    collision = true;
                }
            }

            //----------------------------------------------------------------------------------------

            // scarfyData.rec Object: pos is updated each frame with new pos
            DrawTextureRec(scarfy, scarfyData.rec, scarfyData.pos, WHITE);

            // game logic ends
            EndDrawing();
        }

        // Inside main(), after your primary game loop: IF collision is true, break out of the while loop and enter this loop which creates a game over screen.
        while (!WindowShouldClose())
        {
            BeginDrawing();
            ClearBackground(BLACK);
            if (win)
            {
                DrawText("YOU WIN!", window_width / 2 - MeasureText("YOU WIN!", 40) / 2,
                         window_height / 2 - 50, 40, GREEN);
            }
            else
            {
                DrawText("GAME OVER", window_width / 2 - MeasureText("GAME OVER", 40) / 2,
                         window_height / 2 - 50, 40, RED);
            }
            DrawText("Press R to Restart", window_width / 2 - MeasureText("Press R to Restart", 20) / 2,
                     window_height / 2 + 10, 20, WHITE);
            EndDrawing();

            if (IsKeyPressed(KEY_R))
            {
                break; // Break out of the Game Over/Win loop, and outer loop will then restart game state.
            }
        }
    }
    UnloadTexture(scarfy);
    UnloadTexture(nebula);
    UnloadTexture(background);
    CloseWindow();
}
